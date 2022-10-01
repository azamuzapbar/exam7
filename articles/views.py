from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *
# Create your views here.


def index(request):
        guest = Guest.objects.all()
        form = GuestForm()
        if request.method =='POST':
                form = GuestForm(request.POST)
                if form.is_valid():
                        form.save()
                return redirect('/')
        context = {'guests': guest, 'form': form}
        return render(request, 'main.html', context)

def updateTask(request, pk):
        guest = Guest.objects.get(id=pk)

        form = GuestForm(instance=guest)
        if request.method =='POST':
                form = GuestForm(request.POST, instance=guest)
                if form.is_valid():
                        guest.author=form.cleaned_data['author']
                        guest.email=form.cleaned_data['email']
                        guest.text=form.cleaned_data['text']
                        guest.save()
                return redirect('/')

        context= {'form': form}

        return render(request, 'update_task.html', context)

def deleteTask(request, pk):
        item = Guest.objects.get(id=pk)

        item.delete()
        return redirect('/')



