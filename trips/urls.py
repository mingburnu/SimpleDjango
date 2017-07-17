from rest_framework import routers

from trips.views import PostSet

router = routers.DefaultRouter()
router.register(r'posts', PostSet)
urlpatterns = router.urls
