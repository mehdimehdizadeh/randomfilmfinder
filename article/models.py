from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=150,verbose_name="Title")
    director = models.CharField(max_length=50,verbose_name="Director")
    content = RichTextField(verbose_name="Content")
    value = models.CharField(max_length=150,verbose_name="Value")
    image = models.FileField(blank = True, null = True,verbose_name= "Image")

    def __str__(self):
        return self.title

class Mylist(models.Model):
    user = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    title = models.CharField(max_length=150,verbose_name="Title")
    director = models.CharField(max_length=50,verbose_name="Director")
    image = models.FileField(blank = True, null = True,verbose_name= "Image")
    value = models.CharField(max_length=10,verbose_name="Value",blank=True,null=True)

    def __str__(self):
        return self.title