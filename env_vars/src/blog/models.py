from pyexpat import model
from tabnanny import verbose
from django.db import models
from django.contrib.auth import get_user_model

class Post(models.model):
    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Post"
    post_title = models.CharField(max_length=200)
    post_text = models.TextField()
    post_author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    created_date = models.DateTimeField()
    Published_date = models.DateTimeField()