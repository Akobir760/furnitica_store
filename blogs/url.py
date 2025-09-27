from django.urls import path
from .views import blog_by_category, blog_by_tag

app_name = 'blogs'

urlpatterns = [
    path("category/<int:pk>/", blog_by_category, name="blog_by_category"),
    path("tag/<int:pk>/", blog_by_tag, name="blog_by_tag")
]