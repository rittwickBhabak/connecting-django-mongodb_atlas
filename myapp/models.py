from django.db import models
from django.urls import reverse 

class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()

    def get_absolute_url(self):
        return reverse("myapp:read-post", kwargs={"pk": self.pk})
    
    def __str__(self):
        return self.title 