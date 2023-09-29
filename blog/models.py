from django.db import models
from django.shortcuts import reverse
# Create your models here.


STATUS_CHIOCES = (
    ("pub","Published"),("drf","Draft")
)
class Post(models.Model):

    title = models.CharField(max_length=50)
    text = models.TextField()
    author = models.ForeignKey('auth.user' , on_delete=models.CASCADE)
    date_time_modified = models.DateTimeField(auto_now_add=True)
    date_time_changed = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=50 , choices=STATUS_CHIOCES)

    def __str__(self):
        return self.title
    

    def get_absolute_url(self):
     return reverse('blog_list')