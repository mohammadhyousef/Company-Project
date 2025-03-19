from django.http import HttpResponseRedirect
from .models import Subscriber

def subscribe(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        Subscriber.objects.create(email=email)
        return HttpResponseRedirect('/')