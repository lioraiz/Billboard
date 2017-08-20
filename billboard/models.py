from django.db import models

class Entry(models.Model):
    published = models.DateTimeField('date published')
    title = models.CharField(max_length=100)
    message = models.CharField(max_length=1000)
    author = models.CharField(max_length=100)

    def __str__(self):
        return self.title