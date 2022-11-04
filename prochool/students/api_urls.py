from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api_views import EstablishmentApiViewSet


router = DefaultRouter()

router.register('establishments', EstablishmentApiViewSet)


urlpatterns = [
    path("", include(router.urls))
]
