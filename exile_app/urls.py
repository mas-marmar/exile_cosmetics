from exile_app import views
from django.urls import path

urlpatterns = [
    path('', views.online)
]