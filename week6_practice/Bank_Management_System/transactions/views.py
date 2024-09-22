from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, ListView
from django.views import View
from django.contrib import messages
from django.http import HttpResponse
from datetime import datetime
from django.db.models import Sum
from django.shortcuts import get_object_or_404, redirect
from django.core.mail import EmailMessage,EmailMultiAlternatives
from django.template.loader import render_to_string

from transactions.models import Transaction
from transactions.forms import DepositForm, WithdrawForm, LoanRequestForm, SendMoneyForm
from transactions.constants import DEPOSIT, WITHDRAWAL,LOAN, LOAN_PAID, SEND_MONEY, RECEIVED_MONEY
from accounts.models import UserBankAccount
from core.models import Bank

class TransactionCreateMixin(LoginRequiredMixin, CreateView):
    template_name = 'transaction_form.html'
    model = Transaction
    title = ''
    success_url = reverse_lazy('transaction_report')
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({'account': self.request.user.account})
        return kwargs
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'title': self.title})
        return context

class DepositMoneyView(TransactionCreateMixin):
    form_class = DepositForm
    title = 'Deposit'
    def get_initial(self):
        initial = {'transaction_type': DEPOSIT}
        return initial
    def form_valid(self, form):
        amount = form.cleaned_data.get('amount')
        account = self.request.user.account
        account.balance += amount
        account.save(update_fields=['balance',])
        bank, created = Bank.objects.get_or_create(name='myBank')
        bank.update_balance(amount,'Deposit')
        send_email(self.request.user,amount,'Money Deposit','transaction_mail.html')
        messages.success(
            self.request,
            f'{"{:,.2f}".format(float(amount))}$ was deposited to your account successfully'
        )
        return super().form_valid(form)

class WithdrawMoneyView(TransactionCreateMixin):
    form_class = WithdrawForm
    title = 'Withdraw Money'
    def get_initial(self):
        initial = {'transaction_type': WITHDRAWAL}
        return initial
    def form_valid(self, form):
        amount = form.cleaned_data.get('amount')
        self.request.user.account.balance -= form.cleaned_data.get('amount')
        self.request.user.account.save(update_fields=['balance'])
        bank, created = Bank.objects.get_or_create(name='myBank')
        bank.update_balance(amount,'Withdrawal')
        send_email(self.request.user,amount,'Money Withdrawal','transaction_mail.html')
        messages.success(
            self.request,
            f'Successfully withdrawn {"{:,.2f}".format(float(amount))}$ from your account'
        )
        return super().form_valid(form)

class LoanRequestView(TransactionCreateMixin):
    form_class = LoanRequestForm
    title = 'Request For Loan'
    def get_initial(self):
        initial = {'transaction_type': LOAN}
        return initial
    def form_valid(self, form):
        amount = form.cleaned_data.get('amount')
        current_loan_count = Transaction.objects.filter(
            account=self.request.user.account,transaction_type=3,loan_approve=True).count()
        if current_loan_count >= 3:
            return HttpResponse("You have cross the loan limits")
        send_email(self.request.user,amount,'Loan request','transaction_mail.html')
        messages.success(
            self.request,
            f'Loan request for {"{:,.2f}".format(float(amount))}$ submitted successfully'
        )
        return super().form_valid(form)
    
class TransactionReportView(LoginRequiredMixin, ListView):
    template_name = 'transaction_report.html'
    model = Transaction
    balance = 0
    def get_queryset(self):
        queryset = super().get_queryset().filter(
            account=self.request.user.account
        )
        start_date_str = self.request.GET.get('start_date')
        end_date_str = self.request.GET.get('end_date')
        if start_date_str and end_date_str:
            start_date = datetime.strptime(start_date_str, '%Y-%m-%d').date()
            end_date = datetime.strptime(end_date_str, '%Y-%m-%d').date()
            
            queryset = queryset.filter(timestamp__date__gte=start_date, timestamp__date__lte=end_date)
            self.balance = Transaction.objects.filter(
                timestamp__date__gte=start_date, timestamp__date__lte=end_date
            ).aggregate(Sum('amount'))['amount__sum']
        else:
            self.balance = self.request.user.account.balance
        return queryset.distinct()
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'account': self.request.user.account})
        return context
        
class PayLoanView(LoginRequiredMixin, View):
    def get(self, request, loan_id):
        loan = get_object_or_404(Transaction, id=loan_id)
        print(loan)
        if loan.loan_approve:
            user_account = loan.account
            if loan.amount > user_account.balance:
                messages.error(
                    self.request,
                    f'Loan amount is greater than available balance'
                )
            else:
                user_account.balance -= loan.amount
                loan.balance_after_transaction = user_account.balance
                user_account.save()
                loan.loan_approved = True
                loan.transaction_type = LOAN_PAID
                send_email(self.request.user,loan.amount,'Loan payment','transaction_mail.html')
                loan.save()
                return redirect('loan_list')
                
        return redirect('loan_list')

class LoanListView(LoginRequiredMixin,ListView):
    model = Transaction
    template_name = 'loan_request.html'
    context_object_name = 'loans'
    def get_queryset(self):
        user_account = self.request.user.account
        queryset = Transaction.objects.filter(account=user_account,transaction_type=3)
        print(queryset)
        return queryset

class SendMoneyView(TransactionCreateMixin):
    form_class = SendMoneyForm
    title = 'Send Money'
    def get_initial(self):
        initial = {'transaction_type': SEND_MONEY}
        return initial
    def form_valid(self, form):
        sender_account = self.request.user.account
        receiver_account_no = form.cleaned_data.get('receiver_account')
        receiver_account = UserBankAccount.objects.get(account_no=receiver_account_no)
        amount = form.cleaned_data.get('amount')
        sender_account.balance -= amount
        receiver_account.balance += amount
        receiver_account.save(update_fields=['balance'])
        sender_account.save(update_fields=['balance'])
        send_email(self.request.user,amount,'Send Money','transaction_mail.html')
        send_email(receiver_account.user,amount,'Receival Money','transaction_mail.html')
        Transaction.objects.create(
            account=receiver_account,
            sender_account=sender_account.account_no,
            receiver_account=receiver_account_no,
            amount=amount,
            balance_after_transaction=receiver_account.balance,
            transaction_type = RECEIVED_MONEY  
        )
        messages.success(self.request, f"${amount:.2f} transferred successfully to A/C No.{receiver_account}.")
        return super().form_valid(form)

def send_email(user, amount, subject, template):
        message = render_to_string(template, {
            'user' : user,
            'amount' : amount,
            'subject': subject,
        })
        send_email = EmailMultiAlternatives(subject, '', to=[user.email])
        send_email.attach_alternative(message, "text/html")
        send_email.send()