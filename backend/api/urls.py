from django.urls import path, include
from api import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("cards", views.CardViewSet)

app_name = "api"

urlpatterns = [
    path("", include(router.urls)),
]
