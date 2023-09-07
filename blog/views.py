from django.shortcuts import render
from .models import Post
# Create your views here.





def welcome_page(request):
    return render(request , 'index.html')



def blog_list_view(request):
    post_list = Post.objects.all()
    context = {
        "post_list":post_list
            }
    return render(request , 'blog/blog_list.html' , context=context)



def blog_detail_view(request , pk):

    post_list = Post.objects.get(pk=pk)
    context ={
        "post":post_list
    }
    return render(request , 'blog/blog_detail.html' , context=context)



def blog_new_view(request):


    return render(request, 'blog/blog_new.html' , )