from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.
class post(models.Model):
    STATUS_CHOICES=(
        ('draft','Draft'),
        ('publisher','Publisher'),
    )
  
    title=models.CharField(max_length=250)
    slug=models.SlugField(max_length=250)
    content=models.TextField()
    seo_title=models.CharField(max_length=250)
    seo_description=models.CharField(max_length=160)
    auther=models.ForeignKey(User,on_delete='s',related_name='blog_posts')
    published=models.DateTimeField(default=timezone.now)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
        
    status=models.CharField(max_length=9,choices=STATUS_CHOICES,default="Draft")
    def __str__(self):
        return self.title
    
