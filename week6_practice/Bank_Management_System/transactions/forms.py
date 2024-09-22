from django import forms
from .models import Transaction
from accounts.models import UserBankAccount
from core.models import Bank

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = [
            'amount',
            'transaction_type'
        ]
    def __init__(self, *args, **kwargs):
        self.account = kwargs.pop('account') 
        super().__init__(*args, **kwargs)
        self.fields['transaction_type'].disabled = True 
        self.fields['transaction_type'].widget = forms.HiddenInput()
    def save(self, commit=True):
        self.instance.account = self.account
        self.instance.balance_after_transaction = self.account.balance
        return super().save()

class DepositForm(TransactionForm):
    def clean_amount(self):
        min_deposit_amount = 100
        amount = self.cleaned_data.get('amount')
        if amount < min_deposit_amount:
            raise forms.ValidationError(
                f'You need to deposit at least {min_deposit_amount} $'
            )
        return amount

class WithdrawForm(TransactionForm):
    def clean_amount(self):
        account = self.account
        min_withdraw_amount = 500
        max_withdraw_amount = 100000
        balance = account.balance
        amount = self.cleaned_data.get('amount')
        bank = Bank.objects.get()
        if amount < min_withdraw_amount:
            raise forms.ValidationError(
                f'You can withdraw at least {min_withdraw_amount} $'
            )
        if amount > max_withdraw_amount:
            raise forms.ValidationError(
                f'You can withdraw at most {max_withdraw_amount} $'
            )
        if amount > balance:
            raise forms.ValidationError(
                f'You have {balance} $ in your account. '
                'You can not withdraw more than your account balance'
            )
        if amount > bank.balance:
            raise forms.ValidationError(
                f'Unable to withdraw this amount right now, WE ARE BANKRUPT!'
            )
        return amount

class LoanRequestForm(TransactionForm):
    def clean_amount(self):
        amount = self.cleaned_data.get('amount')
        return amount
    
class SendMoneyForm(TransactionForm):
    class Meta:
        model = Transaction
        fields = ['receiver_account','amount','transaction_type']
    def clean_receiver_account(self):
        receiver_account_no = self.cleaned_data.get('receiver_account')
        try:
            receiver_account = UserBankAccount.objects.get(account_no=receiver_account_no)
        except UserBankAccount.DoesNotExist:
            raise forms.ValidationError("Error: Receiver Account Does not Exist.")
        if self.account.account_no == receiver_account_no:
            raise forms.ValidationError("Error: Cannot send money to yourself!")
        return receiver_account.account_no
    def clean_amount(self):
        account = self.account
        min_send_money = 500
        max_send_money = 20000
        balance = account.balance
        amount = self.cleaned_data.get('amount')
        if amount < min_send_money:
            raise forms.ValidationError(f'You can send at least {min_send_money} $')
        if amount > max_send_money:
            raise forms.ValidationError(f'You can send at most {max_send_money} $')
        if amount > balance:
            raise forms.ValidationError(f'You have {balance} $ in your account. '
                'You cannot send more than your account balance')
        return amount