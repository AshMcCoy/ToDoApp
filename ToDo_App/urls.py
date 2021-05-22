from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name= 'login'),
    path('logout/', LogoutView.as_view(next_page='login'), name= 'logout'),
    path('register/', RegisterPage.as_view(), name= 'register'),
    path('', TaskList.as_view(), name='tasks'),
    path('task/<int:pk>/', TaskDetail.as_view(), name='task'),
    path('task-create/', TaskCreate.as_view(), name = 'task-create'),
    path('task-update/<int:pk>/', TaskUpdate.as_view(), name = 'task-update'),
    path('task-delete/<int:pk>/', TaskDelete.as_view(), name = 'task-delete'),
    path('grocery-list', GroceryList.as_view(), name= 'grocery-list'),
    path('grocery-create', GroceryCreate.as_view(), name= 'grocery-create'),
    path('grocery-update/<int:pk>/', GroceryUpdate.as_view(), name= 'grocery-update'),
    path('grocery-delete/<int:pk>/', GroceryDelete.as_view(), name= 'grocery-delete'),
    path('grocery-complete/<int:id>/', views.grocery_complete, name= 'grocery-complete'),
    path('grocery-incomplete/<int:id>/', views.grocery_incomplete, name= 'grocery-incomplete'),
    path('task-complete/<int:id>/', views.task_complete, name= 'task-complete'),
    path('task-incomplete/<int:id>/', views.task_incomplete, name= 'task-incomplete'),
    path('bill-list', BillList.as_view(), name= 'bill-list'),
    path('bill-create', BillCreate.as_view(), name= 'bill-create'),
    path('bill-update/<int:pk>/', BillUpdate.as_view(), name= 'bill-update'),
    path('bill-delete/<int:pk>/', BillDelete.as_view(), name= 'bill-delete'),
    path('bill-paid/<int:id>/', views.bill_paid, name= 'bill-paid'),
    path('bill-notpaid/<int:id>/', views.bill_notpaid, name= 'bill-notpaid'),

]