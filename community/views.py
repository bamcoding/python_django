from django.shortcuts import render
from community.forms import *

# Create your views here.
def write(request):
    if request.method == 'POST':
        form = Form(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = Form()

    return render(request, 'write.html', {'form':form})

def list(req):
    articleList = Article.objects.all()
    return render (req, 'list.html', {'articleList':articleList})

def view(req, num="1"):
    article = Article.objects.get(id=num)
    return render(req, 'view.html', {'article':article})
