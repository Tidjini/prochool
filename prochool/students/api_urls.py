from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api_views import EstablishmentApiViewSet, ParentApiViewSet, StudentApiViewSet


router = DefaultRouter()

router.register('establishments', EstablishmentApiViewSet)
router.register('parents', ParentApiViewSet)
router.register('students', StudentApiViewSet)


urlpatterns = [
    path("", include(router.urls))
]
