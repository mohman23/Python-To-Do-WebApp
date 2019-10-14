from django.shortcuts import render, redirect
from .models import List    #from models.py import List
from .forms import ListForm #from forms.py import ListForm class.
from django.contrib import messages
from django.http import HttpResponseRedirect

# Create your views here.

def home(request):

    if request.method == 'POST':      # this is to add a new todo list item
        form = ListForm(request.POST or None)

        if form.is_valid():
            form.save()                   #after saving the form return home page(code added below will return home page)
            all_items = List.objects.all  #this is to pull data from the data base
            messages.success(request, ('Item has been added to the list!'))
            return render(request, 'home.html', {'all_items': all_items})
    else:
        all_items = List.objects.all  #this is to pull data from the data base
        return render(request, 'home.html', {'all_items': all_items})

def about(request):
    context = {'first_name' : 'Mohsin', 'last_name' : 'Hafeez'}
    return render(request, 'about.html', context)

def delete(request, list_id):
    item = List.objects.get(pk=list_id) # this is from 0001_initial.py, primary key.
    item.delete()
    messages.success(request, ('Item has been deleted from the list!'))
    return redirect('home')

def cross_off(request, list_id):
    item = List.objects.get(pk=list_id)
    item.completed = True
    item.save()
    return redirect('home')

def uncross(request, list_id):
    item = List.objects.get(pk=list_id)
    item.completed = False
    item.save()
    return redirect('home')

def edit(request, list_id):
    if request.method == 'POST':      # this is to add a new todo list item
        item = List.objects.get(pk=list_id)

        form = ListForm(request.POST or None, instance=item)

        if form.is_valid():
            form.save()                   #after saving the form return home page(code added below will return home page)
            messages.success(request, ('Item has been edited!'))
            return redirect('home')
    else:
        item = List.objects.get(pk=list_id)
        return render(request, 'edit.html', {'item': item})

