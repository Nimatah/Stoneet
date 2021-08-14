from huey.contrib.djhuey import db_task
from django.core.mail import send_mail
from .models import User

SUBJECT = 'تغییر رمز عبور'


@db_task()
def send_reset_password_email(email: str):
    user = User.objects.find_by_email_or_phone_number(email)
    message = f"""
    برای تغییر رمز عبور روی لینک زیر کلیک کنید: \n\n
    https://stoneet.com/users/password-confirmation?token={user.get_password_reset_token()}
    """
    send_mail(subject=SUBJECT, from_email="info@stoneet.com", recipient_list=[user.email], message=message)
