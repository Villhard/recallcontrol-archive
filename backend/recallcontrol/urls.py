from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("cards.urls", namespace="cards")),
    path("accounts/", include("users.urls", namespace="users")),
]
