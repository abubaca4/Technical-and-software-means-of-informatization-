from django.db import models

# Create your models here.

class image_attachment(models.Model):
    picture = models.ImageField()

    def __str__(self):
        return str(self.picture)

class item(models.Model):
    name = models.CharField(max_length = 150)
    description = models.TextField()
    price = models.DecimalField(max_digits=12, decimal_places=2)
    images = models.ManyToManyField(image_attachment)

    def __str__(self):
        return str(self.name)
