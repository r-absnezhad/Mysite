from django.shortcuts import render,get_object_or_404
from blog.models import Post
# Create your views here.
def blog_view(request,**kwargs):
    posts = Post.objects.filter(status = True)
    if kwargs.get('cat_name') != None:
        posts = posts.filter(category__name=kwargs['cat_name'])
    if kwargs.get('author_username') != None :  
        posts = posts.filter(author__username=kwargs['author_username'])    
    content = {'posts': posts}
    return render(request,'blog/blog-home.html',content)

def blog_single(request,pid):
    posts = Post.objects.filter(status = True)
    post = get_object_or_404(posts,pk=pid)
    content = {'post': post}
    return render(request,'blog/blog-single.html',content)

def test(request):
    return render(request,'test.html')

def blog_category(request,cat_name):
    posts = Post.objects.filter(status=1)
    posts = posts.filter(category__name=cat_name)
    context = {'posts': posts}
    return render(request,'blog/blog-home.html',context) 


def blog_search(request):
    posts = Post.objects.filter(status=1)
    if request.method == 'GET':
        if s:= request.GET.get('s'):
            posts = posts.filter(content__contains = s)
    
    context = {'posts': posts}
    return render(request,'blog/blog-home.html',context) 
