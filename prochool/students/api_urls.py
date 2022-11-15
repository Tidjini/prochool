from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api_views import EstablishmentApiViewSet, ParentApiViewSet, StudentApiViewSet, MembershipViewSet


router = DefaultRouter()

router.register('establishments', EstablishmentApiViewSet)
router.register('parents', ParentApiViewSet)
router.register('students', StudentApiViewSet)
router.register('memberships', MembershipViewSet)


urlpatterns = [
    path("", include(router.urls))
]

