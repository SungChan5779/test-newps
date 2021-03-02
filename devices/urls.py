from django.urls import path
from . import views

app_name = "devices"

urlpatterns = [
    path("ups/<int:pk>/", views.Ups_detail, name="ups_detail"),
    path("th/<int:pk>/", views.Th_detail, name="th_detail"),
    path("con/<int:pk>/", views.Con_detail, name="con_detail"),
    # path("Phone/<int:pk>/", views.Phone, name="phone"),
    path("search/", views.Search, name="search"),
    path("ups/", views.Ups, name="ups"),
    path("th/", views.Th, name="th"),
    path("con/", views.Con, name="conn"),
    path("phone_update/<int:pk>/", views.PhoneUpdateView.as_view(), name="phoneupdate"),
]
