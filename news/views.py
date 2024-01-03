from django.shortcuts import render
from .models import News


def home(request):
    notices = {'news': News.objects.all()}
    return render(request, 'home.html', notices)
