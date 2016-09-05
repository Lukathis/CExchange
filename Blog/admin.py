from django.contrib import admin

# Register your models here.
from Blog.models import (
    Article, Category, Author
)


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'abstract', 'body',
                    'author',
                    'create_time', 'last_modified_time',
                    'views', 'thumbs'
                    ]

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['genre']

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['nick_name']