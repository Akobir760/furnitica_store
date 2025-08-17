from pages.views import home_page_view, contact_page_view, blog_page_view, product_page_view, product_checkout_view, product_cart_view, about_page_view, user_wishlist_view
from django.urls import path

app_name = 'pages'

urlpatterns = [
    path('', home_page_view, name='home'),
    path('contact/', contact_page_view, name='contact'),
    path('blog/', blog_page_view, name='blog'),
    path('shop/', product_page_view, name='shop'),
    path('product/cart/', product_cart_view, name='product_cart'),
    path('product/checkout/', product_checkout_view, name='product_checkout'),
    path('about/', about_page_view, name='about'),
    path('user/wishlist/', user_wishlist_view, name='user_wishlist'),
]