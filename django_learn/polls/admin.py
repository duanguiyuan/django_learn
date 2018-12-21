from django.contrib import admin

from .models import Question
from .models import Choice

# 问题 Question 对象需要被管理
admin.site.register(Question)
admin.site.register(Choice)

# Register your models here.
