from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_test_email(email):
    send_mail(
        subject="Test Email",
        message="Celery email task is working!",
        from_email=None,
        recipient_list=[email],
        fail_silently=False,
    )
