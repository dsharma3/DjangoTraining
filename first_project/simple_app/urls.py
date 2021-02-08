from django.urls import path
from simple_app import views
urlpatterns = [
    path('', views.index)
]
