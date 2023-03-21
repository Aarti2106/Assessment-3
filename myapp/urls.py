from django.urls import path
from .import views

urlpatterns = [
    path('',views.index,name='index'),
    path('accounts/',views.accounts,name='accounts'),
    path('products/',views.products,name='products'),
    path('login/',views.login,name='login'),
    path('forgot-password/',views.forgot_password,name='forgot-password'),
    path('verify-otp/',views.verify_otp,name='verify-otp'),
    path('new-password/',views.new_password,name='new-password'),
    path('change-password/',views.change_password,name='change-password'),
    path('logout/',views.logout,name='logout'),
    path('profile/',views.profile,name='profile'),
    path('products/',views.products,name='products'),
    path('add-product/',views.add_product,name='add-product'),
    path('delete_product/<int:pk>/',views.delete_product,name='delete_product'),
    path('profile_view/<int:pk>/',views.profile_view,name='profile_view'),
    ]
