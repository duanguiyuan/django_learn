from django.contrib import admin

from .models import Question
# 问题 Question 对象需要被管理
admin.site.register(Question)

# Register your models here.
