from django.shortcuts import render, redirect, get_object_or_404
from .models import Task

def home_page_view(request):
    tasks = Task.objects.all().order_by('-created_at')
    total_tasks = tasks.count()
    completed_tasks = tasks.filter(completed=True).count()
    pending_tasks = tasks.filter(completed=False).count()
    
    context = {
        'tasks': tasks,
        'total_tasks': total_tasks,
        'completed_tasks': completed_tasks,
        'pending_tasks': pending_tasks,
    }
    return render(request, 'pages/home.html', context)

def add_task_view(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        if title:
            Task.objects.create(title=title.strip())
    return redirect('home')

def toggle_task_view(request, task_id):
    if request.method == 'POST':
        task = get_object_or_404(Task, id=task_id)
        task.completed = not task.completed
        task.save()
    return redirect('home')

def delete_task_view(request, task_id):
    if request.method == 'POST':
        task = get_object_or_404(Task, id=task_id)
        task.delete()
    return redirect('home')
