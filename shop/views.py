from django.shortcuts import render
from .models import CategoryModel

def category_list(request):
    categories = CategoryModel.objects.all()
    return render(request, 'pages/product-grid-sidebar-left.html', {'categories': categories})
