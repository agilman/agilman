from django.db import models

from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel

# Create your models here.
class BlogIndex(Page):
    pass

class BlogPage(Page):
    # title = models.CharField(max_length=64)
    subtitle = models.CharField(max_length=64)
    body = RichTextField(blank=True)
    ds = models.DateField()

    content_panels= Page.content_panels + [
        FieldPanel('subtitle'),
        FieldPanel('body'),
        FieldPanel('ds'),
    ]

    # Parent page / subpage type rules

    parent_page_types = ['blog.BlogIndex']
    subpage_types = []
