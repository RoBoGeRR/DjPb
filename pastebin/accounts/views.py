
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from .forms import RegistrationForm, UserProfileRegistrationForm
from django.conf import settings

def account(request):
    print("if")
    if request.user.is_authenticated:
        print('if')
        if request.user.userprofile.paste_set:
            pastes = request.user.userprofile.paste_set.all()
        else:
            pastes:{}
    return render(request, 'accounts/account.html', context={'pastes':pastes})    
    
# Create your views here.
def login_view(request):
    print("This moment")
    if request.method == 'POST':
        form = AuthenticationForm(request,data=request.POST)
        
        if form.is_valid():
            login(request, form.get_user())
            
            return redirect('home')
    else:
        form = AuthenticationForm()
        print("THIS moment")
    return render(request, 'accounts/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')


def register(request):
    if request.method == 'POST':
        user_form = RegistrationForm(request.POST)
        profile_form = UserProfileRegistrationForm(request.POST, request.FILES)
        if user_form.is_valid(): #and profile_form.is_valid():
            user=user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password'])
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user 
            profile.username = user.username
            profile.password = str(user.password)
            profile.save()
            return redirect('home')
    else:
        user_form = RegistrationForm()
        profile_form = UserProfileRegistrationForm()
    return render(request, 'accounts/register.html', {'user_form': user_form,'profile_form': profile_form})

def home(request):
    return render(request, 'accounts/home.html', )