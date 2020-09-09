from django.shortcuts import render,redirect

# Create your views here.
from django.http import HttpResponse
from django.views.generic import View,ListView
from .forms import AddProducts
from .models import Product,AddCart
from django.contrib import messages


class home(ListView):
   def get(self,request):
       current_user = self.request.user
       return render(request,'shopping/home.html',{'current_user':current_user})

class add(View):
    def get(self,request):
        form = AddProducts()
        return render(request,'shopping/add.html',{'form':form})
    def post(self,request):
        form = AddProducts(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        
        return render(request,'shopping/add.html',{'form':form})

def viewproduct_electronics(request):
    product = Product.objects.get(name='laptop')
    products = Product.objects.filter(category=product.category)
    return render(request,'shopping/viewproduct.html',{'products':products})

def viewproduct_furniture(request):
    product = Product.objects.get(name='sofa')
    products = Product.objects.filter(category=product.category)
    return render(request,'shopping/viewproduct.html',{'products':products})

def add_to_cart(request,pk):
    sel_product = Product.objects.get(id=pk)
    name = sel_product.name
    price = sel_product.price
    cart_product = AddCart(name=name,price=price)
    cart_product.save()
    messages.success(request, 'Added successfully!')
    return redirect(sel_product.get_absolute_url())

   

