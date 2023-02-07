from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('ua/signin', views.sign_in, name="signin"),
    path('ua/regis', views.register, name="register"),
    path('ua/logout', views.logout, name="logout")
]