from django.db import models
from django.db.models.deletion import CASCADE
from django.template.defaultfilters import slugify
from autoslug import AutoSlugField
import random
import string

# Create your models here.


def id_generator():
    return ''.join(random.choices(
        string.ascii_letters + string.digits, k=24))


class Document(models.Model):
    title = models.CharField(max_length=300)
    document_id = models.CharField(max_length=24, default=id_generator)

    def __str__(self):
        return self.title


class Chapter(models.Model):
    document = models.ForeignKey(Document, on_delete=CASCADE)
    title = models.CharField(max_length=100)
    order = models.IntegerField()
    slug = AutoSlugField(populate_from='title')

    def __str__(self):
        return self.title


class Section(models.Model):
    chapter = models.ForeignKey(Chapter, on_delete=CASCADE)
    order = models.IntegerField()
    title = models.CharField(max_length=100)
    content = models.TextField()

    slug = AutoSlugField(populate_from='title')

    def __str__(self):
        return self.title
