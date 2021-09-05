from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.db import models
from django.contrib.auth import login

from apps.users.models import User
from apps.users.tasks import send_reset_password_email


def reset_password_view(request):
    if request.method == 'POST':
        email = request.POST.get('email', None)
        if email is None:
            return render(request, 'users/auth/reset_password.html', context={'error': 'ایمیل یافت نشد'})
        user = User.objects.find_by_email(email=email)
        if user is None:
            return render(request, 'users/auth/reset_password.html', context={'error': 'ایمیل یافت نشد'})
        send_reset_password_email(user)
        return redirect(reverse_lazy('users:password_message'))
    else:
        return render(request, "users/auth/reset_password.html")


def password_message(request):
    return render(request, "users/auth/password_message.html")


def password_confirmation(request):
    token = request.GET.get('token', '')
    try:
        user = User.objects.get_by_token(token)
    except models.fields.exceptions.ValidationError:
        return render(request, "users/auth/password_confirmation.html", context={
            'error': 'لینک مورد نظر منقضی شده'
        })

    if user is None:
        return render(request, "users/auth/password_confirmation.html", context={
            'error': 'لینک مورد نظر منقضی شده'
        })

    if request.method == 'GET':
        return render(request, "users/auth/password_confirmation.html", context={
            'user': user,
        })
    elif request.method == 'POST':
        data = request.POST
        password1 = data.get('password1')
        password2 = data.get('password2')

        if not password1 or not password2:
            return render(request, "users/auth/password_confirmation.html", context={
                'error': 'لطفا رمز عبور را وارد نمایید'
            })

        if password1 != password2:
            return render(request, "users/auth/password_confirmation.html", context={
                'error': 'رمز عبور و تکرار رمز عبور مطابقت ندارند'
            })

        user.set_password(password1)
        user.save()

        login(request, user)
        return redirect(reverse_lazy('users:redirect'))

