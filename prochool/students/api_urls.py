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

# todos: 
#       - is student paied or not 
#            my_memberships.filter(teacher).remain_sessions > 0 and free_membership = False
#       - is student present last course 
#       - get student place or None -> my_places[id]
#       - get student group -> my_places[id].group
#       For details    
#       - get list of presences -> my_presences
#       - get list of payments -> payments
#       - get list of places -> my_places

