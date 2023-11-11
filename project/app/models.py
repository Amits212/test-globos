from django.db import models

class State(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=300)
    image = models.ImageField(upload_to='images/')