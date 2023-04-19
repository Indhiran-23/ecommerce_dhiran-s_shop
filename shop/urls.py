from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('register',views.register,name="register"),
    path('login',views.login_page,name="login"),
    path('logout',views.logout_page,name="logout"),
    path('fav',views.fav_page,name="fav"),
    path('favourite',views.favourite_page,name="favourite"),
    path('remove_favourite/<str:fid>',views.remove_favourite,name="remove_favourite"),
    path('Collections',views.collections,name="collections"),
    path('Collections/<str:name>',views.collectionsview,name="collections"),
    path('Collections/<str:cname>/<str:pname>',views.product_details,name="product_details"),
    path('addtocart',views.add_to_cart,name="addtocart"),
    path('cart',views.cart_page,name="cart"),
    path('remove_cart/<str:cid>',views.remove_cart,name="remove_cart"),
    path('buy/<str:bname>/<str:Bname>',views.buy,name="buy"),

]