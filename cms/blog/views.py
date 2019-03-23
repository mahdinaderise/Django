from django.shortcuts import render
from .models import post
# Create your views here.
#ساخت یک ویو برای نمایش لیست پست ها
def list_of_post(request):
    Post=post.Objects.all()
    template='blog/post/list_of_post.html'
    context={'Post':Post}
    return render(request,template,context)
