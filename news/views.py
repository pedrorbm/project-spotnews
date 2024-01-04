from django.shortcuts import render
from .models import News


def home(request):
    return render(request, "home.html", {"news": News.objects.all()})


def news_details(request, id):
    return render(
        request, "news_details.html", {"new_details": News.objects.get(id=id)}
    )
