from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from putatoe.users.api.views import UserViewSet, DataViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)
router.register("data", DataViewSet)


app_name = "api"
urlpatterns = router.urls
