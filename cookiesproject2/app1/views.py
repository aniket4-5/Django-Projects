from urllib import response
from django.shortcuts import render

# Create your views here.


def home(req):
    print("hii")
    return render(req, 'app1/index.html')


def age(req):
    if req.method == "GET":
        name = req.GET['name']

        response = render(req, 'app1/age.html', {'name': name})
        response.set_cookie('name', name)
        return response


def gf(req):
    if req.method == "GET":
        age = req.GET['age']
        name = req.COOKIES.get('name')
        response = render(req, 'app1/gf.html', {'name': name})
        response.set_cookie('age', age)
        return response


def res(req):
    if req.method == "GET":
        gf = req.GET['gf']
        name = req.COOKIES.get('name')
        age = req.COOKIES.get('age')
        response = render(req, 'app1/res.html',
                          {'name': name, 'age': age, 'gf': gf})
        response.set_cookie('gf', gf)
        return response
