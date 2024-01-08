from django.db import router
from rest_framework_nested import routers

from . import views


router = routers.DefaultRouter()
router.register('products', views.ProductViewSet)


# URLConf
urlpatterns = router.urls


# urlpatterns = router.urls + products_router.urls + carts_router.urls
