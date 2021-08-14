from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
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
        send_reset_password_email(email=email)
        return redirect(reverse_lazy('users:password_message'))
    else:
        return render(request, "users/auth/reset_password.html")


def password_message(request):
    return render(request, "users/auth/password_message.html")


class PasswordConfirmationView(TemplateView):
    template_name = 'users/auth/password_confirmation.html'
