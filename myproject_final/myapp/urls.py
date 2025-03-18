from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_list, name='book_list'),
    path('create/', views.create_book, name='create_book'),
    path('update/<int:id>/', views.update_book, name='update_book'),
    path('delete/<int:id>/', views.delete_book, name='delete_book'),
    
    path('publishers/', views.publisher_list, name='publisher_list'),
    path('publishers/create/', views.create_publisher, name='create_publisher'),
    path('publishers/update/<int:id>/', views.update_publisher, name='update_publisher'),
    path('publishers/delete/<int:id>/', views.delete_publisher, name='delete_publisher'),
]
