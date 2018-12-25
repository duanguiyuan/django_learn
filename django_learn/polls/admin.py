from django.contrib import admin

from .models import Question
from .models import Choice

#class ChoiceInline(admin.StackedInline):
#单行显示
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [('TTT',{'fields':['question_text']}),('Date information', {'fields':['pub_date']}),]
    inlines = [ChoiceInline]
# 问题 Question 对象需要被管理
#admin.site.register(Question)

admin.site.register(Question,QuestionAdmin)
admin.site.register(Choice)

# Register your models here.
