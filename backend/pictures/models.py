from django.db import models

from cloudinary.models import CloudinaryField

# Create your models here.
class Picture(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = CloudinaryField('2022 Mentorship Pictures')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title