from django.db import models
from account.models import User

# Create your models here.



class Profil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    manzil = models.TextField()

    def __str__(self):
        return self.user.username

