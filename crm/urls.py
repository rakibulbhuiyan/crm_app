
from django.urls import path
from crm import views

urlpatterns = [
    path('', views.home, name='home'),
    path('logout/', views.logout_page, name='logout'),
    path('register/', views.register_page, name='Register'),
    path('record/<int:pk>', views.customer_detail, name='record'),
    path('delete/<int:pk>', views.delete_record, name='delete'),
    path('update/<int:pk>', views.update_record, name='update'),
    path('add_record/', views.add_record, name='add_record'),

]
