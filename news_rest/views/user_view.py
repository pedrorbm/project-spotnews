from news_rest.serializers.user_serializer import UserSerializer
from news.models import User

# from rest_framework import routers
# from news_rest.views.category_view import UserViewSet

from rest_framework import viewsets


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer

    queryset = User.objects.all()
