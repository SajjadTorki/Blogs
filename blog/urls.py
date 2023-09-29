from django.urls import path

from .views import *

urlpatterns = [
    path('', welcome_page , name="home_page"),
    path('blog/',BlogListView.as_view() , name="blog_list"),
    path('blog/<int:pk>',BlogDetailView.as_view() , name="blog_detail"),
    path("blog/new/", BlogNewView.as_view(), name="blog_new"),
    path('blog/<int:pk>/update/', BlogUpdateView.as_view() , name="blog_update"),
    path('blog/<int:pk>/delete/', BlogDeleteView.as_view(), name="blog_delete"),

]
