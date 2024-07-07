from django import template
from blog.models import Post
register = template.Library()

@register.simple_tag (name='totalposts')
def function():
    posts = Post.objects.filter(status=1).count()
    return posts


@register.simple_tag (name='posts')
def function():
    posts = Post.objects.filter(status=1)
    return posts

@register.filter
def snippet(value,args =15):
    return value[:args] +'...'


@register.inclusion_tag('blog/blog-popular-posts.html')
def latestposts():
    posts = Post.objects.filter(status=1).order_by('published_date')[:2]
    return {'posts': posts}