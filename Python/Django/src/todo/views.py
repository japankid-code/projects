from django.shortcuts import render

def index(request):
    context = {}
    return render(request, 'todo/index.html', context)