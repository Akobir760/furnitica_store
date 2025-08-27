from django.db import models
from django.utils.translation import gettext_lazy as _


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class BlogCategoryModel(BaseModel):
    name = models.CharField(max_length=100, unique=True, verbose_name=_('category_name'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')


class TagModel(BaseModel):
    name = models.CharField(max_length=50, unique=True, verbose_name=_('tag_name'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Tag')
        verbose_name_plural = _('Tags')


class ComentModel(BaseModel):
    blog = models.ForeignKey('BlogModel', on_delete=models.CASCADE, related_name='comments', verbose_name=_('blog'))
    email = models.EmailField(verbose_name=_('email'))
    text = models.TextField(verbose_name=_('text'))

    def __str__(self):
        return f'Comment by {self.email} on {self.blog.title}'

    class Meta:
        verbose_name = _('Comment')
        verbose_name_plural = _('Comments')    

class BlogModel(BaseModel):
    title = models.CharField(max_length=200)
    category = models.ForeignKey(BlogCategoryModel, on_delete=models.CASCADE, related_name=_('blogs'))
    image = models.ImageField(upload_to='images/', blank=True, null=True, verbose_name=_('image'))
    short_description = models.TextField(verbose_name=_('shorgt_description'))
    long_description = models.TextField(verbose_name=_('long_description'))
    tags = models.ManyToManyField(TagModel, blank=True, related_name='blogs', verbose_name=_('tags'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Blog')
        verbose_name_plural = _('Blogs')
