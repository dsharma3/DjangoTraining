from django.db import models

# # Create your models here.
class Topic(models.Model):
    topic_name = models.CharField(max_length=250, unique=True)

    def __str__(self):
        return self.topic_name

class Website(models.Model):
    website_name = models.CharField(max_length=400)
    url = models.URLField()
    topic = models.ForeignKey(Topic, on_delete=models.PROTECT)


    def __str__(self):
        return self.website_name
    