from django.db import models

from wagtail.models import Page

class HomePage(Page):
    subpage_types = ['blog.BlogIndex']
    parent_page_types = ['wagtailcore.Page']
    max_count = 1 
