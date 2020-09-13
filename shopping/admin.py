from django.contrib import admin

# Register your models here.
from .models import Category,Product,Profile,Buy,AddCart

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(AddCart)
admin.site.register(Profile)
admin.site.register(Buy)


