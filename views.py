from django.http import HttpResponse
from django.shortcuts import render, redirect
from authapp.forms import RegisterForm, EditProfileForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required


# Create your views here.


def welcome(request):
    return HttpResponse('Welcome page renders out')


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('auth:welcome')

    context = {'form': RegisterForm()}
    return render(request, 'authapp/register.html', context)


@login_required(login_url='/auth/login')
def profile(request):
    context = {'user': request.user}
    return render(request, 'authapp/profile.html', context)


@login_required(login_url='/auth/login')
def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(data=request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('auth:welcome')

    context = {'form': EditProfileForm(instance=request.user)}
    return render(request, 'authapp/edit_profile.html', context)


@login_required(login_url='/auth/login')
def password_change(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            return redirect('auth:welcome')

    context = {'form': PasswordChangeForm(user=request.user)}
    return render(request, 'authapp/password_change_form.html', context)


@login_required(login_url='/auth/login')
def logout_view(request):
    logout(request)
    return redirect('auth:login')
