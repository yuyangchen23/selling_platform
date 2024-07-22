from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ClientViewSets

router = DefaultRouter()
router.register(r'clients', ClientViewSets)

urlpatterns = [
    path("", include(router.urls))
]