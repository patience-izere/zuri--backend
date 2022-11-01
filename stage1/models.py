from django.db import models

# Create your models here.
class zuriModel(models.Model):
    slackUsername = models.CharField(max_length=200)
    backend = models.BooleanField()
    age = models.IntegerField()
    bio = models.CharField(max_length=500)

    def __str__(self):
        return self.slackUsername
