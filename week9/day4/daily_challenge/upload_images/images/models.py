from django.db import models

# Create your models here.
class Image(models.Model):
    img = models.ImageField(upload_to='posts/')
    timestamp = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ["-timestamp"]