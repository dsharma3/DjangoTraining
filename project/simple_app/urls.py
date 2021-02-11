from django.urls import path
from simple_app import views
urlpatterns = [
    path('', views.contact_us_django),
    path('websites',views.display_websites)
]
