from rest_framework import routers
from measurements.views import ProjectViewSet, MeasurementViewSet

router = routers.DefaultRouter()
router.register('api/project', ProjectViewSet, 'project')
router.register('api/measurement', MeasurementViewSet, 'measurement')

urlpatterns = router.urls
