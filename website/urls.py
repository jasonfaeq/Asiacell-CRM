from django.urls import path
from . import views # Import views from current directory

urlpatterns = [
    path("", views.home, name="home"),
    path("logout/", views.logout_user, name="logout"), # its views.logout_user so it wont conflict with the impored logout
    path('record/<int:pk>/', views.customer_record, name='record'),
    path('delete/<int:pk>/', views.delete_customer, name='delete'), 
    path('add_record/', views.add_record, name='add_record'),
    path('update/<int:pk>/', views.update_record, name='update'), 
]
# Path: website/views.py