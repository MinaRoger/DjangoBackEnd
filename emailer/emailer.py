from django.core.mail import send_mail
from mytut.settings import EMAIL_HOST_USER
from celery import shared_task


@shared_task
def send_welcome_email(email, name):
    send_mail(
        'Welcome!' + name,
        'Here is the message.',
        EMAIL_HOST_USER,
        [email],
        fail_silently=False
    )
