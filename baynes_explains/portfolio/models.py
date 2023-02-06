from django.db import models
from django.urls import reverse


# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=100)
    content = models.TextField()
    link = models.URLField()
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('project-detail', kwargs={'pk': self.pk})