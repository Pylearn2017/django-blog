from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='hello'),
    path('a/', views.a, name='a')
]
