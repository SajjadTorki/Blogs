from django.shortcuts import render

# Create your views here.





def welcome_page(request):
    return render(request , 'index.html')



def blog_list_view(request):
    return render(request , 'blog/blog_list.html')