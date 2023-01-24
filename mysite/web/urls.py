from django.urls import path
from . import views

app_name = "web"   


urlpatterns = [

    path("web/", views.index, name="index"),
]