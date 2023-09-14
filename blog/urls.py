from django.urls import path

from .views import welcome_page,blog_list_view,blog_detail_view,blog_new_view,blog_edit_view

urlpatterns = [
    path('', welcome_page , name="home_page"),
    path('blog/',blog_list_view , name="blog_list"),
    path('blog/<int:pk>',blog_detail_view , name="blog_detail"),
    path("blog/new/", blog_new_view, name="blog_new"),
    path('blog/<int:pk>/edite', blog_edit_view, name="blog_edit"),
]
