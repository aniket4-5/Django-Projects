from django.http import HttpResponseRedirect
from django.shortcuts import render, HttpResponse
from .forms import Empreg
from .models import Emp
# Create your views here.


def home(req):
    if req.method == 'POST':
        fm = Empreg(req.POST)
        if fm.is_valid():
            fm.save()
            fm = Empreg()
            return HttpResponseRedirect('/')
    else:
        fm = Empreg()
    data = Emp.objects.all()
    return render(req, 'enroll/index.html', {'form': fm, 'data': data})


def update_data(req, id):
    if req.method == 'POST':
        pi = Emp.objects.get(pk=id)
        fm1 = Empreg(req.POST, instance=pi)
        if fm1.is_valid():
            fm1.save()
            return HttpResponseRedirect('/')

    else:
        pi = Emp.objects.get(pk=id)
    fm1 = Empreg(instance=pi)
    return render(req, 'enroll/update.html', {'form': fm1})


def delete_data(req, id):
    if req.method == 'POST':
        pi = Emp.objects.get(pk=id)
        pi.delete()
    return HttpResponseRedirect('/')
