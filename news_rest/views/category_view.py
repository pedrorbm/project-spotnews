from news.models import Category
from rest_framework import viewsets

# from rest_framework import routers
# from news_rest.views.category_view import CategoryViewSet

from news_rest.serializers.category_serializer import CategorySerializer


class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer

    queryset = Category.objects.all()
