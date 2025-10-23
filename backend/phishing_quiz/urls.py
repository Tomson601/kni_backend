from django.urls import path
from . import views

urlpatterns = [
    path('get_top_players/', views.get_top_players),
    path('save_result/', views.save_result),
]