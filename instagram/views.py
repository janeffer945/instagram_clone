from django.shortcuts import render
from .models import post
from django.views.generic import(ListView

)  
# Create your views here.
class postview(ListView):
     template_name ="insta/post_list.html"
     queryset =post.objects.all()
     content_object_name='posts'