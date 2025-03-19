from django.core.management.base import BaseCommand
from newsletter.models import Subscriber
from faker import Faker

class Command(BaseCommand):
    help = 'Seed the email subscribers table with test data'

    def handle(self, *args, **kwargs):
        fake = Faker()
        for _ in range(1000):  # Add 1000 test subscribers
            Subscriber.objects.create(email=fake.email())
        self.stdout.write(self.style.SUCCESS('Successfully seeded subscribers'))