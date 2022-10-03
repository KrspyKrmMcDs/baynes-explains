from django.db import models

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=100)
    content = models.TextField()
    youtube_link = models.URLField()
    
    def __str__(self):
        return self.name