from django.shortcuts import render,redirect

# Create your views here.
from django.http import HttpResponse
from django.views.generic import View,ListView
from .forms import AddProducts,RegisterFrom,LoginForm,ProfileForm
from .models import Product,Profile, Buy,AddCart
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User 
from django.contrib import auth


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
    current_user = request.user
    sel_product = Product.objects.get(id=pk)
    name = sel_product.name
    price = sel_product.price
    cart_product = AddCart(name=name,price=price)
    cart_product.save()
    messages.success(request, 'Added successfully!')
    # important
    return redirect(request.META['HTTP_REFERER'])
    #return redirect(request.META['HTTP_REFERER'])

#class buy(ListView):
    #def get(self,request,pk):
def buy(request,pk):
        buy_product = AddCart.objects.get(id=pk)
        buy_product.delete()
        name = buy_product.name
        price = buy_product.price
        Buy.objects.create(name=name,price=price)
        b_product = Buy.objects.all()
        return render(request,'shopping/mycart.html',{'b_product':b_product})
        

def remove_from_cart(request,pk):
    sel_product = AddCart.objects.get(id=pk)
    sel_product.delete()
    return redirect('mycart')


#class viewcart(ListView):
    #model = AddCart
    #template_name = 'shopping/mycart.html'
def viewcart(request):
    cart_product = AddCart.objects.all()
    return render(request,'shopping/mycart.html',{'cart_product':cart_product})

def register(request):
    form = RegisterFrom()
    if request.method=='POST':
        form = RegisterFrom(request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')
            confirm_password = request.POST.get('confirm_password')
            hash_password = make_password(password)
            if password != confirm_password:
                error = 'password doesnot match'
                return render(request,'shopping/register.html',{'form':form,'error':error})
            User.objects.create(username=username,email=email,password=hash_password)
            return redirect('login')
    return render(request,'shopping/register.html',{'form':form})


def login(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')
        login_user = auth.authenticate(username=username,password=password)

        if login_user is not None:
            auth.login(request,login_user)
            return redirect('profile')

    return render(request,'shopping/login.html',{'form':form})

def profile(request):
    #pro = Profile.objects.get(id=pk)
    current_user = request.user
    #model = current_user.profile_set.all()
    form = ProfileForm(instance=request.user.profile)
    if request.method =='POST':
        form = ProfileForm(request.POST,instance=request.user.profile)
        if form.is_valid():
            #f_name = request.POST.get('first_name')
            #l_name = request.POST.get('last_name')
            #address = request.POST.get('address')
            #ph_num = request.POST.get('phone_number')
            #p_user = Profile(user=current_user,first_name=f_name,
            #last_name=l_name,address=address,phone_number=ph_num )
            #print('up save')
            #p_user.save() 
            form.save()
          
        else:
            print('else')
            #return redirect('/')
    context = {'form':form,'current_user':current_user}
    return render(request,'shopping/profile.html',context)

