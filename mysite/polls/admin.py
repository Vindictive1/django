from django.contrib import admin

from .models import Question, Choice


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    #
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    # 过滤器，可以按 pub_date 字段来过滤列表
    list_filter = ['pub_date']
    # 在列表的顶部增加一个搜索框
    search_fields = ['question_text']


admin.site.register(Question, QuestionAdmin)
