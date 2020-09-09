from django.db import models

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=100)
    primarycategory = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category,on_delete= models.CASCADE)
    description = models.CharField(max_length=100)
    price = models.FloatField()

    def __str__(self):
        return self.name

class AddCart(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()

    def __str__(self):
        return self.name



