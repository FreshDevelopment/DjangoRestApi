from rest_framework.routers import DefaultRouter
from category.api.views import CategoryApiViewSet

router_categories = DefaultRouter()

router_categories.register(prefix = 'category', basename = 'category', viewset = CategoryApiViewSet)