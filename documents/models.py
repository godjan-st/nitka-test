from django.db import models

class Document(models.Model):
    name = models.CharField(max_length=255)
    text = models.TextField()
    image = models.ImageField(upload_to='documents/')

    def __str__(self):
        return self.name