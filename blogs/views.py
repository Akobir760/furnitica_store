from django.shortcuts import render

from . models import BlogCategoryModel, BlogModel, TagModel

def blog_by_category(request, pk):
    try:
        category = BlogCategoryModel.objects.get(pk=pk)
    except BlogCategoryModel.DoesNotExist:
        return render(request=request, template_name='pages/404.html')
    
    blogs = BlogModel.objects.filter(category=category)

    return render(request=request, template_name='pages/blog-list-sidebar-left.html', context={
        'category': category,
        'blog': blogs
    })


def blog_by_tag(request, pk):
    try:
        tag = TagModel.objects.get(pk=pk)
    except TagModel.DoesNotExist:
        return render(request=request, template_name='pages/404.html')
    
    blog = BlogModel.objects.filter(tags=tag)

    return render(request=request, template_name='pages/blog-list-sidebar-left.html', context={
        'tag':tag,
        'blog': blog
    })