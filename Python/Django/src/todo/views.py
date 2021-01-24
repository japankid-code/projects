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


def completeTodo(request, todo_id):
    todo = Todo.objects.get(pk=todo_id)
    todo.complete = True
    todo.save()

    return redirect('index')


def deleteCompleted(request):
    Todo.objects.filter(complete__exact=True).delete()

    return redirect('index')
