from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .api_views import GroupApiViewSet, PlaceApiViewSet

router = DefaultRouter()

router.register('groups', GroupApiViewSet)
router.register('places', PlaceApiViewSet)


urlpatterns = [
    path('', include(router.urls))
]
