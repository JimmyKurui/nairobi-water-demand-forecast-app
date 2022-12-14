from django.urls import path
from . import views


urlpatterns = [
    path('', views.homepage, name="index"),
    path('/dashboard', views.dashboard, name="dashboard"),
    path('/contribute', views.contribute, name="contribute"),
    path('/support', views.support, name="support"),
    path('/about', views.about, name="about"),
]
