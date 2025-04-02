from django.urls import path
from . import views

urlpatterns = [
    path("", views.org_chart_view, name="org_chart"),
    path('department_list/', views.department_list, name='department_list'),
    path('department_edit/', views.department_edit, name='department_edit'),
]