from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Subscriber
from .forms import SubscribeForm
from .tasks import send_email_batch
import redis

def subscribe(request):
    if request.method == 'POST':
        form = SubscribeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success_view')  # Replace with your success view
    else:
        form = SubscribeForm()
    return render(request, 'newsletter/subscribe.html', {'form': form})

def send_email_view(request):
    if request.method == 'POST':
        subject = request.POST['subject']
        message = request.POST['message']
        subscriber_ids = list(Subscriber.objects.values_list('id', flat=True))
        batch_ids = [subscriber_ids[i:i + 10] for i in range(0, len(subscriber_ids), 10)]
        try:
            for batch in batch_ids:
                send_email_batch.delay(batch, subject, message)
            return redirect('success_view')  # Replace with your success view
        except redis.ConnectionError:
            messages.error(request, "Failed to connect to the Redis server. Please try again later.")
            return redirect('send_email')
    return render(request, 'newsletter/send_email.html')