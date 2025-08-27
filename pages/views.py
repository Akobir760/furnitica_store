from django.shortcuts import render
from shop.models import CategoryModel, ProductModel, CatalogModel
from blogs.models import BlogCategoryModel, BlogModel, TagModel, ComentModel

def home_page_view(request):
    return render(request=request, template_name='home.html')

def contact_page_view(request):
    return render(request=request, template_name='pages/contact.html')


def blog_page_view(request):
    categories = BlogCategoryModel.objects.all()
    blogs = BlogModel.objects.all()
    tags = TagModel.objects.all()
    context = {
        'categories': categories,
        'blogs': blogs,
        'tags': tags
    }

    return render(request=request, template_name='pages/blog-list-sidebar-left.html', context=context)

def product_page_view(request):
    categories = CategoryModel.objects.all()   
    products = ProductModel.objects.all() 
    catalogs = CatalogModel.objects.all()
    context = {
        'categories': categories,
        'products': products,
        'catalogs': catalogs
    }
    return render(request, 'pages/product-grid-sidebar-left.html', context)
def product_cart_view(request):
    return render(request=request, template_name='pages/product-cart.html')

def product_checkout_view(request):
    return render(request=request, template_name='pages/product-checkout.html')

def about_page_view(request):
    return render(request=request, template_name='pages/about-us.html')


def user_wishlist_view(request):
    return render(request=request, template_name='pages/user-wishlist.html')

