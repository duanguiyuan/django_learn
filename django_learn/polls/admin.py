from django.contrib import admin

from .models import Question
from .models import Choice

class QuestionAdmin(admin.ModelAdmin):
    fields = ['pub_date', 'question_text']

# 问题 Question 对象需要被管理
#admin.site.register(Question)

admin.site.register(Question,QuestionAdmin)
admin.site.register(Choice)

# Register your models here.
