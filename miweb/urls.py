from django.urls import path
from miweb import views


urlpatterns = [
    path("", views.index, name="home"),
]
