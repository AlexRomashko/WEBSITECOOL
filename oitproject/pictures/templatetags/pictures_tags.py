from django import template
import pictures.views as views


register = template.Library()


@register.simple_tag()
def getCategories():
    return views.cats_db


@register.inclusion_tag('pictures/articles.html')
def show_categories(cat_selected=0):
    cats = views.cats_db
    return {'cats': cats, 'cat_selected': cat_selected}