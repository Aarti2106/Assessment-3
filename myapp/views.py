from django.shortcuts import render
from .models import Products,User
from django.conf import settings
from django.core.mail import send_mail
import random
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def index(request):
    return render(request,'index.html')

def accounts(request):
    if request.method=="POST":
        try:
            user=User.objects.get(email=request.POST['email'])
            msg="Email Alredy Regiostered"
            return render(request,'accounts.html',{'msg':msg})
        except:
            if request.POST['password']==request.POST['password2']:
                User.objects.create(
                    name=request.POST['name'],
                    email=request.POST['email'],
                    phone=request.POST['phone'],
                    password=request.POST['password'],
                    photo=request.FILES['upload_new_photo'],
                    usertype=request.POST['usertype']
                    )
                msg="User Sign Up Successfully"
                return render(request,'accounts.html',{'msg':msg})
            else:
                msg="Password & Confirm Password Does Not Matched"
                return render(request,'accounts.html',{'msg':msg})
    else:
        return render(request,'accounts.html')

def products(request):
    return render(request,'products.html')

def login(request):
    if request.method=='POST':
        try:
            user=User.objects.get(email=request.POST['email'])
            if user.password==request.POST['password']:
                request.session['email']=user.email
                request.session['fname']=user.name
                print(user.photo.url)
                request.session['profile_pic']=user.photo.url
                return render(request,'index.html')
            else:
                msg="Incorrect Password"
                return render(request,'login.html',{'msg':msg})
        except Exception as e:
            print(e)
            msg="Email Not Registered"
            return render(request,'login.html',{'msg':msg})
    else:
        return render(request,'login.html')

    return render(request,'login.html')
def logout(request):
    try:
        del request.session['email']
        del request.session['fname']
        del request.session['profile_pic']
        return render(request,'login.html')
    except:
        return render(request,'login.html')

def forgot_password(request):
    if request.method=='POST':
        try:
            user=User.objects.get(email=request.POST['email'])
            otp=random.randint(1000,9999)
            subject = 'OTP For Forgot Password'
            message = 'Hello User ,Your OTP For Forgot Password Is :'+str(otp)
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [user.email, ]
            send_mail( subject, message, email_from, recipient_list )
            return render(request,'otp.html',{'email':user.email,'otp':otp}) 
        except Exception as e:
            print(e)
            msg="Email Not Registered"
            return render(request,'forgot-password.html',{'msg':msg})
    else:
        return render(request,'forgot-password.html')
    
def verify_otp(request):
    email=request.POST['email']
    otp=request.POST['otp']
    uotp=request.POST['uotp']

    if otp==uotp:
        return render(request,'new-password.html',{'email':email})
    else:
        msg="Invalid OTP"
        return render(request,'otp.html',{'email' : email,'otp' : otp,'msg' : msg}) 
def new_password(request):
    email=request.POST['email']
    np=request.POST['new_password']
    cnp=request.POST['cnew_password']

    if np==cnp:
        user=User.objects.get(email=email)
        user.password=np
        user.save()
        msg="Password Updated Successfully"
        return render(request,'login.html',{'msg':msg})
    else:
        msg="New Password & Confirm Password Does Not Matched"
        return render(request,'new-password.html',{'email':email,'msg':msg})


def change_password(request):
    if request.method=="POST":
        user=User.objects.get(email=request.session['email'])
        if user.password==request.POST['old_password']:
            if request.POST['new_password']==request.POST['cnew_password']:
                user.password=request.POST['new_password']
                user.save()
                msg="Password Changed Successfully"
                return redirect('logout')
            else:
                msg="New password & Confirm New Password Does Note Matched"
                return render(request,'change-password.html',{'msg':msg})
        else:
            msg="Old password Does Note Matched"
            return render(request,'change-password.html',{'msg':msg})
    else:
        return render(request,'change-password.html')
def profile(request):
    user=User.objects.get(email=request.session['email'])
    if request.method=="POST":
        user.name=request.POST['name']
        user.email=request.POST['email']
        user.phone=request.POST['phone']
        user.password=request.POST['password']
        try:
            user.photo=request.FILES['upload_new_photo']
        except:
            pass
        user.save()
        request.session['profile_pic']=user.photo.url
        msg="Profile Updated Successfully"
        return render(request,'profile.html',{'user':user,'msg':msg})
    else:
        return render(request,'profile.html',{'user':user})
def products(request):
    product=Products.objects.all()
    return render(request,'products.html',{'product':product})

def add_product(request):
    user=User.objects.get(email=request.session['email'])
    if request.method=="POST":
        Products.objects.create(
                user=user,
                product_category=request.POST['product_category'],
                product_name=request.POST['product_name'],
                product_stock=request.POST['product_stock'],
                product_desc=request.POST['product_desc'],
                product_expire_date=request.POST['product_expire_date'],
                product_image=request.FILES['product_image']
            )
        msg="Product Added Successfully"
        return render(request,'add-product.html',{'msg':msg})
    else:
        return render(request,'add-product.html')
def delete_product(request,pk):
    product=Products.objects.get(pk=pk)
    product.delete()
    return render(request,'add-product.html')
def profile_view(request,pk):
    product=Products.objects.get(pk=pk)
    if request.method=="POST":
        product.product_name=request.POST['product_name']
        product.product_desc=request.POST['product_desc']
        product.product_stock=request.POST['product_stock']
        product.product_expire_date=request.POST['product_expire_date']
        try:
            product.product_image=request.FILES['product_image']
        except:
            pass
        product.save()
        msg="Profile Updated Successfully"
        return render(request,'profile-view.html',{'product':product,'msg':msg})
    else:
        return render(request,'profile-view.html',{'product':product})

