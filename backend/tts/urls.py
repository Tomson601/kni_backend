from django.urls import path
from .views import tts

urlpatterns = [
    path('tts/', tts),
]