from django.urls import path, include
from rest_framework.routers import DefaultRouter


from .api_views import PaymentApiViewSet

router = DefaultRouter()
router.register('payments', PaymentApiViewSet)


urlpatterns = [
    path('', include(router.urls))
]
