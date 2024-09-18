from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name="index"),
    path('delete-transaction/<id>/',views.delete_transaction,name='delete_transaction'),
    path('login/', views.login_view,name = "login_"),
    path('register/',views.register_view,name = "register_"),
    path('logout',views.logout_view,name="logout_view")
]
