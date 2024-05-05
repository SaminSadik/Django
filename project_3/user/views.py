from .forms import signupForm, ProfileForm, PassForm1, PassForm2
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash

# Create your views here.
def signup(request):
    if(request.method == 'POST'):
        form = signupForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Account created successfully')
            form.save()
            return redirect('signin')
    else:
        form = signupForm()
        messages.info(request, 'Welcome to Signup Page')
    return render(request, 'signup.html', {'form': form})

def signin(request):
    if not request.user.is_authenticated:
        if(request.method == 'POST'):
            form = AuthenticationForm(request, data=request.POST) # in-built login form
            if form.is_valid():
                uname = form.cleaned_data['username']
                # AuthenticationForm has 'username' & 'password' field
                upass = form.cleaned_data['password']
                # checking if username & password matches in the database
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'You are now logged in')
                    return redirect('profile')
                else: # if name or pass is wrong, authenticate returns None
                    messages.error(request, 'Invalid username or password')
        else:
            form = AuthenticationForm()
        return render(request, 'signin.html', {'form': form})
    
    else: # if already logged in, can't access signin page
        messages.warning(request, 'You are already logged in')
        return redirect('profile')

def profile(request):
    if request.user.is_authenticated:
        return render(request, 'profile.html', {'user': request.user})
    else: # can't access if not logged in
        messages.warning(request, 'Please login to access your profile')
        return redirect('signin')
    
@login_required # same as requiring user.is_authenticated True to access
def signout(request):
    logout(request) # built-in method to logout the user
    messages.success(request, 'You are now logged out')
    return redirect('signin')
    
@login_required # needs LOGIN_URL in settings.py to redirect to a designated login url
def edit_info(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile Updated Successfully')
            return redirect('profile')
    else:
        form = ProfileForm(instance=request.user) # to display the current user details
    return render(request, 'edit.html', {'form':form})

@login_required # if LOGIN_URL is not set to a valid login page, it will redirect to 'page not found'
def edit_pass(request):
    if request.method == 'POST':
        form = PassForm1(request.user, request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Password Changed Successfully')
            update_session_auth_hash(request, form.user) # required to secure changed password
            return redirect('profile')
    else:
        form = PassForm1(user=request.user)
    return render(request, 'edit.html', {'form':form, 'txt':'Forgot Password ?'})

@login_required
def for_pass(request):
    if request.method == 'POST':
        form = PassForm2(request.user, request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Password Changed Successfully')
            update_session_auth_hash(request, form.user)
            return redirect('profile')
    else:
        form = PassForm2(user=request.user)
    return render(request, 'edit.html', {'form':form})