from .models import Subscriber

def run():
    emails = [
        'test1@example.com',
        'test2@example.com',
        'test3@example.com',
        ...
    ]

    for email in emails:
        Subscriber.objects.create(email=email)