from django.contrib import admin

# Register your models here.
from .models import Article,Mylist

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title','director']
    list_display_links = ['title']
    search_fields = ['title','director']

    class Meta:
        model = Article
        
@admin.register(Mylist)
class MylistAdmin(admin.ModelAdmin):
    list_display = ['user','title','director']

