from django.contrib import admin

from .models import Grade,Subject, Year, QuestionPaper, Motivation

admin.site.register(Grade)
admin.site.register(Subject)
admin.site.register(Year)
admin.site.register(QuestionPaper)
admin.site.register(Motivation)

