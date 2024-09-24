from django.urls import path
from cards import views

app_name = "cards"

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("cards/", views.CardListView.as_view(), name="card_list"),
    path("cards/create/", views.CardCreateView.as_view(), name="card_create"),
    path("cards/update/<int:pk>/", views.CardUpdateView.as_view(), name="card_update"),
    path("cards/delete/<int:pk>/", views.CardDeleteView.as_view(), name="card_delete"),
]
