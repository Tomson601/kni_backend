# from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('api/', include('phishing_quiz.urls')),
    path('api/', include('tts.urls')),
]
