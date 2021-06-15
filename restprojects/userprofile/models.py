from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Profile(models.Model):
    photo = models.ImageField(null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=30)
    wallet = models.PositiveIntegerField(default=0)
    count_order = models.PositiveIntegerField(default=0)
    sale = models.FloatField(default=0.0)

    def __str__(self):
        return self.full_name


