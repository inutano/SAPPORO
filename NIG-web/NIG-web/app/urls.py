# coding: utf-8
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from . import views

app_name = "app"

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("login/", LoginView.as_view(), name="signin"),
    path("logout/", LogoutView.as_view(), name="signout"),
    path("signup/", views.SignupView.as_view(), name="signup"),
    path("machine/", views.MachineListView.as_view(), name="machine_list"),
    path("job/", views.JobListView.as_view(), name="job_list"),
    path("data/", views.DataListView.as_view(), name="data_list"),
    path("<str:user_name>/", views.UserDetailView.as_view(), name="user_detail"),
]