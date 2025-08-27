from django.shortcuts import render
from .models import CategoryModel, ProductModel, CatalogModel

def product_by_category(request, pk):
    try:
        category = CategoryModel.objects.get(pk=pk)
    except CategoryModel.DoesNotExist:
        return render(request=request, template_name="pages/404.html")
    
    products = ProductModel.objects.filter(category=category)
    return render(request=request, template_name="pages/product-grid-sidebar-left.html", context={
        "categoty": category, 
        "products": products})


def product_by_catalog(request, pk):
    try:
        catalog = CatalogModel.objects.get(pk=pk)
    except CatalogModel.DoesNotExist:
        return render(request=request, template_name="pages/404.html")
    
    product = ProductModel.objects.filter(catalog=catalog)
    return render(request=request, template_name="pages/product-grid-sidebar-left.html", context={
        "catalog": catalog, 
        "product": product})