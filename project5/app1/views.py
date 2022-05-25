from django.shortcuts import render
from app1.models import Post
from app1.form import addPostForm
# Create your views here.


def index(req):
    return render(req, 'app1/index.html')


def addPost(req):
    form = addPostForm()
    if req.method == 'POST':
        form = addPostForm(req.POST)
        if form.is_valid():
            form.save()
        return index(req)
    return render(req, 'app1/addPost.html', {'form': form})


def show(req):
    post_data = Post.objects.all()
    print(post_data)
    my_dict = {'data': post_data}
    return render(req, 'app1/showPost.html', context=my_dict)
