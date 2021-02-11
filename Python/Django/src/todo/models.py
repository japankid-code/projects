from django.shortcuts import render
from django.db import models

def index(request):
    context = {}
    return render(request, 'todo/index.html', context)

class Todo(models.Model):
    text = models.CharField(max_length=40)
    complete = models.BooleanField(default=False)

    def __str__(self):
        return self.text