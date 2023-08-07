from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("<int:numb>", views.monthly_numb),
    path("<str:month>", views.monthly_challenge, name="monthly-challenge"),
]
