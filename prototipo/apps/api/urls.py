

from django.contrib import admin
from django.urls import path, include

from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

from .views import (HelloView,
                    ProfileViewSet,
                    RegistroViewSet,
                    UserViewSet,
                    GroupViewSet,
                    UserDataView)

router = routers.DefaultRouter()
router.register(r'profiles', ProfileViewSet)
router.register(r'registros', RegistroViewSet)
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)


urlpatterns = [
    path('hello/', HelloView.as_view(), name='hello'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),

    path('', include(router.urls)),
    # path('registros2/', api_views.RegistroListView.as_view(), name='regidtro-list2')
]
