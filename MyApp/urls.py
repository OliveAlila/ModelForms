from django.urls import path
from MyApp import views

urlpatterns = [
  path('', views.home, name='my_home')
]
