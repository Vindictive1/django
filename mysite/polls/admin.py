from django.contrib import admin

from .models import Question


class QuestionAdmin(admin.ModelAdmin):
    # 在管理界面，顺序为 pub_date, question_text
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]


admin.site.register(Question, QuestionAdmin)
