from django.contrib import admin
from .models import Article, Comment

class CommentInline(admin.TabularInline):
    model = Comment

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','date','author','comment_count',)
    inline = [
        CommentInline,
    ]

# Register your models here.
admin.site.register(Article, ArticleAdmin)

admin.site.register(Comment)