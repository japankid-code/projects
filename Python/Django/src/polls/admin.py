from django.contrib import admin

from .models import Choice, Question

# Register your models here.

class ChoiceInLine(admin.StackedInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,                  {'fields': ['question_text']}),
        ('Date Information',    {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inLines = [ChoiceInLine]

admin.site.register(Question, QuestionAdmin)