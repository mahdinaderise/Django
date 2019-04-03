from django.shortcuts import render,get_object_or_404
from .models import post
# Create your views here.
#ساخت یک ویو برای نمایش لیست پست ها
def list_of_post(request):
    Post=post.objects.all()
    template='blog/post/list_of_post.html'
    context={'Post':Post}
    return render(request,template,context)
def post_detail(request,slug):
    post=get_object_or_404(post,slug=slug)
    template='blog/post/post_detail.html'
    context={'Post':Post}
    return render(request,template,context)