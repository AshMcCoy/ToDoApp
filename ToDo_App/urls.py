from django.urls import path
from .views import TaskCreate, TaskList, TaskDetail, TaskCreate, TaskUpdate, TaskDelete, CustomLoginView, RegisterPage, GroceryList, GroceryCreate, GroceryUpdate, GroceryDelete
from django.contrib.auth.views import LogoutView

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

]