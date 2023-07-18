from rest_framework import viewsets
from DemoCodeBase.user.models import Users
from DemoCodeBase.user.serializers import UsersSerializer


class UsersViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer

