from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    digital = models.BooleanField(default=False, null=True, blank=True)
    description = models.TextField(blank=True, null=True)
    image = models.FileField(upload_to='images')

    def __str__(self):
        return self.name

