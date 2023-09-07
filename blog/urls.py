from django.urls import path

from .views import welcome_page,blog_list_view,blog_detail_view

urlpatterns = [
    path('', welcome_page , name="home_page"),
    path('blog/',blog_list_view , name="blog_list"),
    path('blog/<int:pk>',blog_detail_view , name="blog_detail"),

]
