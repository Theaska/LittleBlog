from django import template
from blog.models import Blog

register = template.Library()

@register.filter(name='months_list')
def months_list(value):
        value = ['january', 'february', 'march', 'april', 'may', 'june',
                'july', 'august', 'september', 'october', 'november', 'december']
        return value

@register.filter(name='get_blogs_tags')
def get_blogs_tags(value):
        value = Blog.objects.values('tagline')
        return value
