from django.shortcuts import render
from .models import Subscriber
from .forms import SubscriptionForm 
from django.http import HttpResponse

def subscribe(request):
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'newsletter/thank_you.html')
    else:
        form = SubscriptionForm()
    return render(request, 'newsletter/subscribe.html', {'form': form})


def send_email_view(request):
 
    return HttpResponse("تم إرسال البريد الإلكتروني بنجاح.")