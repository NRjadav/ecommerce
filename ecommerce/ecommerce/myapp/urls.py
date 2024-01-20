"""
URL configuration for ecommerce project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('',views.index,name="index"),
    path('cart',views.cart,name="cart"),
    path('checkout',views.checkout,name="checkout"),
    path('contact',views.contact,name="contact"),
    path('detail',views.detail,name="detail"),
    path('detail1/<int:id>',views.detail1,name="detail1"),
    path('add_to_cart/<int:id>',views.add_to_cart,name="add_to_cart"),
    path('cart_plus/<int:id>',views.cart_plus,name="cart_plus"),
    path('cart_minus/<int:id>',views.cart_minus,name="cart_minus"),
    path('cart_remove/<int:id>',views.cart_remove,name="cart_remove"),
    path('shop',views.shop,name="shop"),
    path('login',views.login,name="login"),
    path('logout',views.logout,name="logout"),
    path('register',views.register,name="register"),
    path('search',views.search,name="search"),
   
   
]





