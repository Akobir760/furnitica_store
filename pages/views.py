from django.shortcuts import render

def home_page_view(request):
    return render(request=request, template_name='home.html')

def contact_page_view(request):
    return render(request=request, template_name='pages/contact.html')


def blog_page_view(request):
    return render(request=request, template_name='pages/blog-list-sidebar-left.html')

def product_page_view(request):
    return render(request=request, template_name='pages/product-grid-sidebar-left.html')

def product_cart_view(request):
    return render(request=request, template_name='pages/product-cart.html')

def product_checkout_view(request):
    return render(request=request, template_name='pages/product-checkout.html')

def about_page_view(request):
    return render(request=request, template_name='pages/about-us.html')


def user_wishlist_view(request):
    return render(request=request, template_name='pages/user-wishlist.html')

