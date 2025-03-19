import django_rq
from django.core.mail import send_mail
from .models import Subscriber

@django_rq.job
def send_email_batch(subscriber_ids, subject, message):
    subscribers = Subscriber.objects.filter(id__in=subscriber_ids)
    for subscriber in subscribers:
        send_mail(subject, message, 'your-email@example.com', [subscriber.email])