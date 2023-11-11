from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_world, name='world'),
    path('index/', views.get_all_states, name='index')
]