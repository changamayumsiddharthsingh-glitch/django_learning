from django.shortcuts import render, redirect, get_object_or_404
from .models import Task, Page, GalleryImage

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

def page_detail_view(request, slug):
    # This fetches the Page from the database that matches the slug in the URL.
    # We also check that is_published=True so hidden pages aren't viewable.
    page = get_object_or_404(Page, slug=slug, is_published=True)
    
    # We pass the page object to a template to render it.
    return render(request, 'pages/page_detail.html', {'page': page})

def gallery_view(request):
    # Fetch all images from the database, newest first
    images = GalleryImage.objects.all().order_by('-uploaded_at')
    return render(request, 'pages/gallery.html', {'images': images})

