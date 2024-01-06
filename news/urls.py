from django.urls import path

# from rest_framework import routers
# from news_rest.views.category_view import CategoryViewSet

from .views import home, news_details, categories_form, news_form

urls = [
    path("", home, name="home-page"),

    path("news/<int:id>/", news_details, name="news-details-page"),

    path("categories/", categories_form, name="categories-form"),

    path("news/", news_form, name="news-form"),
]

urlpatterns = urls
