from django.urls import path, include
from . import views
urlpatterns = [
    path('get/', views.testing),
]