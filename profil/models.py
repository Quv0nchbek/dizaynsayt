from django.db import models
from account.models import User
from django.db import models
from django.dispatch import Signal

from django.utils import timezone
from django.db.models.signals import post_save
# Create your models here.



class Profil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profil_img', default='images/logo.jpg', blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    manzil = models.TextField()

    def __str__(self):
        return self.user.username


def create_profil(sender, instance, created, **kwargs):
    if created:
        Profil.objects.create(
            user=instance
        )

Signal.connect(post_save, create_profil, sender=User)