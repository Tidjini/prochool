from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api_views import EstablishmentApiViewSet, ParentApiViewSet


router = DefaultRouter()

router.register('establishments', EstablishmentApiViewSet)
router.register('parents', ParentApiViewSet)


urlpatterns = [
    path("", include(router.urls))
]
