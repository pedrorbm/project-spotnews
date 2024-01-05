from django.shortcuts import render, redirect
from .forms import CategoryForm
from .models import News


def home(request):
    return render(request, "home.html", {"news": News.objects.all()})


def news_details(request, id):
    return render(
        request, "news_details.html", {"new_details": News.objects.get(id=id)}
    )


def categories_form(request):
    if request.method == "POST":
        if CategoryForm(request.POST).is_valid():

            return redirect('home-page')

    elif request.method != "POST":
        form = CategoryForm()

    return render(request, 'categories_form.html', {'form': form})
