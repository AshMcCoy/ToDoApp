from django.shortcuts import render, redirect 
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import Task, Grocery, Bill
from django.contrib import messages
import bcrypt

class CustomLoginView(LoginView):
    template_name= 'ToDo_App/login.html'
    fields= '__all__'
    redirect_authenticated_user= True
    
    def get_success_url(self):
        return reverse_lazy('tasks')

class RegisterPage(FormView):
    template_name= 'ToDo_App/register.html'
    form_class= UserCreationForm
    redirect_authenticated_user= True
    success_url= reverse_lazy('tasks')

    def form_valid(self, form):
        user= form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('tasks')
        return super(RegisterPage, self).get(*args, **kwargs)


class TaskList(LoginRequiredMixin, ListView):
    model = Task
    context_object_name= 'tasks'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks']= context['tasks'].filter(user=self.request.user)
        context['count']= context['tasks'].filter(complete=False).count()
        
        search_input = self.request.GET.get('search-area') or ''
        if search_input: 
            context['tasks'] = context['tasks'].filter(title__startswith=search_input)

        context['search_input'] = search_input

        return context

class TaskDetail(LoginRequiredMixin, DetailView):
    model= Task
    context_object_name= 'task'
    template_name= 'ToDo_App/task.html'

class TaskCreate(LoginRequiredMixin, CreateView):
    model= Task
    fields = ['title', 'description', 'complete', 'category', 'due_date']
    success_url= reverse_lazy('tasks')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreate, self).form_valid(form)

class TaskUpdate(LoginRequiredMixin, UpdateView):
    model= Task
    fields= ['title', 'description', 'complete', 'category', 'due_date']
    success_url= reverse_lazy('tasks')

class TaskDelete(LoginRequiredMixin, DeleteView):
    model= Task
    context_object_name= 'task'
    success_url= reverse_lazy('tasks')    

class GroceryList(LoginRequiredMixin, ListView):
    model = Grocery
    context_object_name= 'groceries'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['groceries']= context['groceries'].filter(user=self.request.user)
        context['count']= context['groceries'].filter(complete=False).count()
        
        search_input = self.request.GET.get('search-area') or ''
        if search_input: 
            context['groceries'] = context['groceries'].filter(item__startswith=search_input)

        context['search_input'] = search_input

        return context

class GroceryCreate(LoginRequiredMixin, CreateView):
    model= Grocery
    fields = ['item', 'category', 'complete']
    success_url= reverse_lazy('grocery-list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(GroceryCreate, self).form_valid(form)

class GroceryUpdate(LoginRequiredMixin, UpdateView):
    model= Grocery
    fields= ['item', 'category', 'complete']
    success_url= reverse_lazy('grocery-list')

class GroceryDelete(LoginRequiredMixin, DeleteView):
    model= Grocery
    context_object_name= 'groceries'
    success_url= reverse_lazy('grocery-list')

def grocery_complete(request, id):
    mark_complete = Grocery.objects.get(id=id)
    mark_complete.complete=True;
    mark_complete.save()
    return redirect('/grocery-list')

def grocery_incomplete(request, id):
    mark_complete = Grocery.objects.get(id=id)
    mark_complete.complete=False;
    mark_complete.save()
    return redirect('/grocery-list')

def task_complete(request, id):
    mark_complete = Task.objects.get(id=id)
    mark_complete.complete=True;
    mark_complete.save()
    return redirect('/')

def task_incomplete(request, id):
    mark_complete = Task.objects.get(id=id)
    mark_complete.complete=False;
    mark_complete.save()
    return redirect('/')

class BillList(LoginRequiredMixin, ListView):
    model = Bill
    context_object_name= 'bills'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['bills']= context['bills'].filter(user=self.request.user)
        context['count']= context['bills'].filter(paid=False).count()
        
        search_input = self.request.GET.get('search-area') or ''
        if search_input: 
            context['bills'] = context['bills'].filter(item__startswith=search_input)

        context['search_input'] = search_input

        return context

class BillCreate(LoginRequiredMixin, CreateView):
    model= Bill
    fields = ['bill', 'category', 'due_date', 'paid']
    success_url= reverse_lazy('bill-list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(BillCreate, self).form_valid(form)

class BillUpdate(LoginRequiredMixin, UpdateView):
    model= Bill
    fields= ['bill', 'category', 'due_date', 'paid']
    success_url= reverse_lazy('bill-list')

class BillDelete(LoginRequiredMixin, DeleteView):
    model= Bill
    context_object_name= 'bills'
    success_url= reverse_lazy('bill-list')

def bill_paid(request, id):
    mark_paid = Bill.objects.get(id=id)
    mark_paid.paid=True;
    mark_paid.save()
    return redirect('/bill-list')

def bill_notpaid(request, id):
    mark_notpaid = Bill.objects.get(id=id)
    mark_notpaid.paid=False;
    mark_notpaid.save()
    return redirect('/bill-list')