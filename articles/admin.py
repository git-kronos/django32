from django.contrib import admin
from .models import Article


# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    '''
        Admin View for
    '''
    list_display = ('id', 'title',)
    # list_filter = ('',)
    # inlines = [
    #     Inline,
    # ]
    # raw_id_fields = ('',)
    readonly_fields = ('id',)
    search_fields = ('title', 'content')


admin.site.register(Article, ArticleAdmin)
