from django.shortcuts import render
from community.models import Article
import datetime
#from community.forms import *

# Create your views here.
def write(req):
    if req.method == 'POST':
        title = req.POST['title']
        contents = req.POST['contents']
        post = Article(title=title)
        post.contents=contents
        post.lastDate = datetime.datetime.now()
        post.save()

    return render(req, 'write.html')

def doWrite(req):
    if req.method == 'POST':
        title = req.POST['title']
        name = req.POST['name']
        contens = req.POST['contents']



# def list(req):
#     if req.method == 'POST':
#
#
#     articleList = Article.objects.all()
#     return render (req, 'list.html', {'articleList':articleList})
#
# def view(req, num="1"):
#     article = Article.objects.get(id=num)
#     return render(req, 'view.html', {'article':article})
