from rest_framework import routers
from .api import projectViewset

router = routers.DefaultRouter()

router.register('api/projects', projectViewset, 'projects')

urlpatterns = router.urls
