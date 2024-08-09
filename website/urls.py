from django.urls import path
from . import views # Import views from current directory

urlpatterns = [
    path("", views.home, name="home"),
    path("logout/", views.logout_user, name="logout"),
    path('record/<int:pk>/', views.customer_record, name='record'),
    path('delete/<int:pk>/', views.delete_customer, name='delete'), 
    path('add_record/', views.add_record, name='add_record'),
    path('update/<int:pk>/', views.update_record, name='update'), 
    path('export/', views.export_csv, name='export'),
    path('about/', views.about, name='about'),
]
# Path: website/views.py