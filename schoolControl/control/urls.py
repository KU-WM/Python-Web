from django.urls import path
from . import views

urlpatterns = [
    path('control/', views.userList, name='user'),
    path('control/login', views.userLogin, name='login'),
    # path('control/student/', views.userLogin, name='order_create'),
    # path('control/lecture/', views.userLogin, name='order_create'),
    # path('control/instructor/', views.userLogin, name='order_create'),
]