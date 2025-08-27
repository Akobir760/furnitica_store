from django.urls import path
from .views import product_by_category, product_by_catalog

app_name = 'shop'

urlpatterns = [
    path("category/<int:pk>/", product_by_category, name="product_by_category"),
    path("catalog/<int:pk>/", product_by_catalog, name="product_by_catalog")
]
