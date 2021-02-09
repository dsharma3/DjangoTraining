from django.contrib import admin
from simple_app.models import Topic
from simple_app.models import Website

# Register your models here.
admin.site.register(Topic)
admin.site.register(Website)