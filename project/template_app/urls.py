from django.urls import path
from template_app import views
urlpatterns = [
    path('', views.index),
    path('index', views.index, name='index'),
    path('aboutus', views.aboutus, name='aboutus'),
    path('contactus', views.contactus, name='contactus'),
    path('employee/',views.employee, name='employee'),
    path('employee/list',views.employee_list, name='employeelist'),
]
