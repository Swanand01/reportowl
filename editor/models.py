from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.


class Document(models.Model):
    title = models.CharField(max_length=300)

    def __str__(self):
        return self.title


class Chapter(models.Model):
    document = models.ForeignKey(Document, on_delete=CASCADE)
    title = models.CharField(max_length=100)
    order = models.IntegerField()

    def __str__(self):
        return self.title


class Section(models.Model):
    chapter = models.ForeignKey(Chapter, on_delete=CASCADE)
    order = models.IntegerField()
    title = models.CharField(max_length=100)
    content = models.TextField()

    def __str__(self):
        return self.title
