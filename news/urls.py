from django.urls import path
from . import views

urls = [
    path("", views.home, name="home-page"),
    path("news/<int:id>/", views.news_details, name="news-details-page"),
    path("categories/", views.categories_form, name="categories-form"),
]

urlpatterns = urls
