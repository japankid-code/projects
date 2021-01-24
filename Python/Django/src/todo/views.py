from django.shortcuts import render

def index(request):
    context = {}
    return render(request, 'todo/index.html', context)

def addTodo(request):
    form = TodoForm(request.POST)

    if form.is_valid():
        new_todo = Todo(text=request.POST['text'])
        new_todo.save()

    return redirect('index')