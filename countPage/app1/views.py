from django.shortcuts import render

# Create your views here.


def count_view(req):
    count = int(req.COOKIES.get('count', 0))
    newCount = count+1
    respone = render(req, 'app1/index.html', {'count': newCount})
    respone.set_cookie('count', newCount, max_age=10)
    return respone
