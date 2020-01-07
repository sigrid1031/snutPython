from django.shortcuts import render, redirect
from .models import Coupon, User, UserCoupon

# Create your views here.

def main(request):
    
    context = {
        'coupons' : Coupon.objects.all()
    }
    
    return render(request, "coupon/main.html", context)

def login(request):
    return render(request, "coupon/login.html")

def create(request):
    if request.method =="GET":
        hp = request.GET.get('hp')
        
        coupon_id = request.GET.get('coupon_idx')
        if User.objects.filter(hp=hp).exists()==False:
            User.objects.create(hp=hp)
            
        user = User.objects.get(hp=hp)
        coupon = Coupon.objects.get(pk=coupon_id)
        
        UserCoupon.objects.create(user=user, coupon=coupon)
        return redirect('/')
        