import datetime as dt
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import LoginForm


# User = get_user_model()


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST or None)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,
                                email=cd.get('email'),
                                password=cd.get('password'))
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Аутентификация пройдена')
                else:
                    return HttpResponse('Аккаунт отключен')
            else:
                return HttpResponse('Ошибка аутентификации')
    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login')


# декоратор это проверка регистрации текущего пользователя
@login_required
def dashboard(request):
    return render(request,
                  'account/dashboard.html',
                  {'selection': 'dashboard'})  # переменная для подсвечивания
#
#
# def logout_view(request):
#     logout(request)
#     return redirect('account:login')
#
#
# def register_view(request):
#     form = UserRegistrationForm(request.POST or None)
#     if form.is_valid():
#         new_user = form.save(commit=False) # записываем пользователя, но пока без пароля
#         new_user.set_password(form.cleaned_data['password']) # зашифровка пароля
#         new_user.save()
#         messages.success(request, 'Пользователь добавлен в систему.')
#         return render(request, 'account/register_done.html',
#                       {'new_user': new_user})
#     return render(request, 'account/register.html', {'form': form})
