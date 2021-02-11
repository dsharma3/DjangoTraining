import os
# from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'first_project.settings')
# settings.configure()

import django
django.setup()

import random
from simple_app.models import Topic, Website
from faker import Faker

fakeGen = Faker()

topic = ['Search', 'Social', 'Marketplace', 'News', 'Games']

def add_topic():
    t = Topic.objects.get_or_create(topic_name = random.choice(topic))[0]
    t.save()
    return t

def populateWebsite(N = 5):
    for entry in range(N):
        topic = add_topic()

        fake_url = fakeGen.url()
        fake_name = fakeGen.company()
        
        webSite = Website.objects.get_or_create(topic=topic,url = fake_url, website_name = fake_name)[0]
        webSite.save()

if __name__== '__main__':
    print("populating data")
    populateWebsite(50)
    print("population complete")

        