from django.test import TestCase 

from celery import shared_task
from django.core.mail import send_mail 
from .models import Subscriber

@shared_task
def send_newsletter_email(subject, message):
    subscribers = Subscriber.objects.values_list('email', flat=True)
    batch_size = 25
    for i in range(0, len(subscribers), batch_size):
        send_mail(subject, message, 'admin@company.com', subscribers[i:i+batch_size])
    return f'Sent to {len(subscribers)} subscribers'
