from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Category, Page, Comment
from django.db.models import Q

def post_list_view(request):
    posts = Post.objects.filter(status='published')
    
    # Search functionality
    query = request.GET.get('q')
    if query:
        posts = posts.filter(
            Q(title__icontains=query) | Q(content__icontains=query)
        )
        
    categories = Category.objects.all()
    pages = Page.objects.filter(status='published')
    
    context = {
        'posts': posts,
        'categories': categories,
        'pages': pages,
    }
    return render(request, 'blog/post_list.html', context)

def post_detail_view(request, slug):
    post = get_object_or_404(Post, slug=slug, status='published')
    categories = Category.objects.all()
    pages = Page.objects.filter(status='published')
    
    # Handle Comment Submission
    if request.method == 'POST':
        author_name = request.POST.get('author_name')
        content = request.POST.get('content')
        if author_name and content:
            Comment.objects.create(post=post, author_name=author_name, content=content)
            return redirect('blog:post_detail', slug=post.slug)
    
    comments = post.comments.all()
    
    context = {
        'post': post,
        'categories': categories,
        'pages': pages,
        'comments': comments,
    }
    return render(request, 'blog/post_detail.html', context)

def category_posts_view(request, slug):
    category = get_object_or_404(Category, slug=slug)
    posts = category.posts.filter(status='published')
    categories = Category.objects.all()
    pages = Page.objects.filter(status='published')
    
    context = {
        'category': category,
        'posts': posts,
        'categories': categories,
        'pages': pages,
    }
    return render(request, 'blog/post_list.html', context)

def page_detail_view(request, slug):
    page = get_object_or_404(Page, slug=slug, status='published')
    categories = Category.objects.all()
    pages = Page.objects.filter(status='published')
    
    context = {
        'page': page,
        'categories': categories,
        'pages': pages,
    }
    return render(request, 'blog/page_detail.html', context)
