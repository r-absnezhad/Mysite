from django.shortcuts import render,get_object_or_404
from blog.models import Post
# Create your views here.
def blog_view(request):
    posts = Post.objects.filter(status = True)
    content = {'posts': posts}
    return render(request,'blog/blog-home.html',content)
def blog_single(request):
    return render(request,'blog/blog-single.html')
def test(request,pid):
    post = get_object_or_404(Post,pk=pid)
    content = {'post': post}
    return render(request,'test.html',content)