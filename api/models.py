from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Vechicles(models.Model):
    name=models.CharField(max_length=100)
    model=models.CharField(max_length=100)
    brand=models.CharField(max_length=100)
    colour=models.CharField(max_length=100)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    price=models.CharField(max_length=100)
    is_active=models.BooleanField(default=True)


class VecicleImage(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    vechicle=models.ForeignKey(Vechicles,on_delete=models.CASCADE)
    image=models.ImageField(null=True,upload_to="vechicleimage")

class Wishlist(models.Model):
    vechicle=models.ForeignKey(Vechicles,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    options=(
        ("pending","pending"),
        ("cancelled","cancelled"),
        ("approved","approved")
            )
    status=models.CharField(max_length=100,choices=options,default="pending")

class Sales(models.Model):
    vechicle=models.ForeignKey(Vechicles,on_delete=models.CASCADE)
    customer=models.ForeignKey(User,on_delete=models.CASCADE)
    price=models.PositiveIntegerField()