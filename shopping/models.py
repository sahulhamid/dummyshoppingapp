from django.db import models
from django.db.models.signals import post_delete,pre_save,post_save
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

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
    #user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    price = models.FloatField()

    def __str__(self):
        return self.name

class Buy(models.Model):
   
    name = models.CharField(max_length=100)
    price = models.FloatField()

    def __str__(self):
        return self.name
    

def added_to_cart(sender,instance,**kwargs):
    print('itme has been added to cart')

post_save.connect(added_to_cart,sender=AddCart)

def deleted_from_cart(sender,instance,**kwargs):
    print('item removed from cart')

post_delete.connect(deleted_from_cart,sender=AddCart)


class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address = models.TextField()
    # phone number using regular expression
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$')
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True) # validators should be a list
    def __str__(self):
        return str(self.user)


def profile_created(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user=instance)
        print('saved')

post_save.connect(profile_created,sender=User)

#def profile_update(sender,instance,created,**kwargs):
    #if created == False:
       # instance.profile.save()
        #print('updated')

#post_save.connect(profile_update,sender=User)
    

