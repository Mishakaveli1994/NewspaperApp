from django.contrib import admin
from .models import Article, Comment


# class CommentInline(admin.StackedInline): - Stacked
class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0  # To not display 3 empty rows


class ArticleAdmin(admin.ModelAdmin):
    inlines = [
        CommentInline,
    ]


admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment)
