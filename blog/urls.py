from django.urls import path

from .views import *

urlpatterns = [
    path('', welcome_page , name="home_page"),
    path('blog/',blog_list_view , name="blog_list"),
    path('blog/<int:pk>',blog_detail_view , name="blog_detail"),
    path("blog/new/", blog_new_view, name="blog_new"),
    path('blog/<int:pk>/update/', blog_edit_view, name="blog_update"),
    path('blog/<int:pk>/delete/', blog_delete_view, name="blog_delete"),

]
