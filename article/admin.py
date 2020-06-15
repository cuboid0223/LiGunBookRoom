from django.contrib import admin

# Register your models here.
from article.models import Article, Comment

#客製化管理者頁面
class CommentAdmin(admin.ModelAdmin):
    list_display=['article', 'content','pubDateTime']
    list_display_link=['article']# 設定資料連結欄位，透過article來連結
    list_filter=['article', 'content'] # 設定過濾器，點選文章標題及會列出所屬留言
    search_fields = ['content'] # 設定搜尋欄位
    list_editable = ['content'] # 設定編輯欄位
    class Meta:
        model = Comment


admin.site.register(Article)
admin.site.register(Comment,CommentAdmin)