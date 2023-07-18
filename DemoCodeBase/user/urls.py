from django.urls import path
from DemoCodeBase.user.viewsets import UsersViewSet

urlpatterns = [
    path('', UsersViewSet.as_view({
        'get': 'list',
        'post': 'create',
    })),
    path('<int:pk>', UsersViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy',
    })),
]
