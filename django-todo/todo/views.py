from django.shortcuts import render
from .forms import TaskForm

# Create your views here.
def index(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
    

    form = TaskForm()
    context = {'form': form}

    return render(request, 'todo/index.html', context=context)

def add(request):
    return

def complete(request):
    return