from django.shortcuts import render,get_object_or_404,redirect
from blog.models import Post,Comment
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from blog.forms import CommentForm
from django.contrib import messages
from django.urls import reverse
from django.http import HttpResponseRedirect
# Create your views here.
def blog_view(request,**kwargs):
    posts = Post.objects.filter(status = True)
    if kwargs.get('cat_name') != None:
        posts = posts.filter(category__name=kwargs['cat_name'])
    if kwargs.get('author_username') != None :  
        posts = posts.filter(author__username=kwargs['author_username'])    
    if kwargs.get('tag_name') != None :  
        posts = posts.filter(tags__name__in=[kwargs['tag_name']])
    posts = Paginator(posts,3)
    try:
        page_number=request.GET.get('page')
        posts=posts.get_page(page_number)
    except PageNotAnInteger:
        posts=posts.get_page(1)
    except EmptyPage:
        posts=posts.get_page(1)

    
    content = {'posts': posts}
    return render(request,'blog/blog-home.html',content)

def blog_single(request,pid): 
    posts = Post.objects.filter(status = True)
    post = get_object_or_404(posts,pk=pid)
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,'YOUR COMMENT SUBMITED CORRECTLY')
        else:
            messages.add_message(request,messages.ERROR,'YOUR COMMENT DID NOT SUBMITED')
                 
    
    if post.login_required and not request.user.is_authenticated:
        next_url = request.get_full_path()  # Current URL with query parameters
        return redirect(f'{reverse("accounts:login")}?next={next_url}')
    
    comments = Comment.objects.filter(post=post.id, approved=True)
    form = CommentForm()
    content = {'post': post, 'comments': comments, 'form': form}
    return render(request, 'blog/blog-single.html', content)


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
