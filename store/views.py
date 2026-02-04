from django.shortcuts import render
from .models import Product
# Create your views here.
def home(request):
    products=Product.objects.filter(is_approved=True)
    return render(request,'store/home.html',{'products':products})

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Product, Category

@login_required
def shop(request):
    # Sirf admin-approved products dikhane ke liye
    products = Product.objects.filter(is_approved=True)

    # Categories sidebar/filter ke liye
    categories = Category.objects.all()

    context = {
        'products': products,
        'categories': categories
    }

    return render(request, 'store/shop.html', context)
