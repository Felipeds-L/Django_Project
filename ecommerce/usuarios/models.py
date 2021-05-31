from django.db import models
from django.db.models.base import Model

# Create your models here.

class Usuario(models.Model):
    user_name = models.CharField(max_length=20)
    pass_user = models.CharField(max_length=20)

    def __str__(self):
        return self.user_name

class Produto(models.Model):
    prod_name = models.CharField(max_length=40)
    prod_price = models.CharField(max_length=10)
    prod_seller = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return self.prod_name, self.prod_price, self.prod_seller