from django.urls import path
from devices import views as devices_views


app_name = "core"

urlpatterns = [
    path("", devices_views.HomeView, name="home")
]
