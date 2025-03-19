import django_rq
from django.core.mail import send_mail
from .models import Subscriber

def send_emails(message):
    subscribers = Subscriber.objects.all()
    for subscriber in subscribers:
        send_mail(
            'Newsletter',
            message,
            'from@example.com',
            [subscriber.email],
            fail_silently=False,
        )

def send_emails_job(message):
    queue = django_rq.get_queue('default')
    queue.enqueue(send_emails, message)