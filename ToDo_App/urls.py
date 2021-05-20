from django.urls import path
from .views import TaskList
from . import views

app_name = 'ToDo_App'

urlpatterns = [
    #path('', index, name = "index"),
    path('', TaskList.as_view(), name='tasks'),

]