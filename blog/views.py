from time import timezone
from urllib import request
from django.shortcuts import get_object_or_404, render
from django.utils import timezone
from blog.models import Post

# Create your views here.
def index(request):
    posts = Post.objects.filter(published_at__lte=timezone.now())
    return render(request, "blog/index.html", {"posts": posts})


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, "blog/post-detail.html", {"post": post})
