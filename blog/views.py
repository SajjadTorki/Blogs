from django.shortcuts import render , redirect
from .models import Post
from .forms import NewPostForm

# Create your views here.





def welcome_page(request):
    return render(request , 'index.html')



def blog_list_view(request):
    post_list = Post.objects.filter(status ="pub")
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
    if request.method == "POST":
        form = NewPostForm(request.POST)
        if form.is_valid():
            form.save()
            form = NewPostForm()
            return redirect("blog_list")

    else :
     form = NewPostForm()
     
    return render(request, 'blog/blog_new.html' ,context={"form":form} )



def blog_edit_view(request ):    
    
     
    

    return render(request , "blog/blog_new.html",)
    