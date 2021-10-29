from django.shortcuts import render
from .models import Document, Chapter, Section

# Create your views here.


def index(request):
    context = {}
    if request.method == "POST":
        title = request.POST['title1']
        content = request.POST['content1']
        doc = Document(title="Document 1")
        doc.save()
        chapter = Chapter(document=doc, title="Literature Survey", order=1)
        chapter.save()
        section = Section(chapter=chapter, title=title,
                          content=content, order=1)
        section.save()
        context = {'title1': title}

    if Section.objects.filter(title="xyz").exists():
        section = Section.objects.get(title="xyz")
        context['content1'] = section.content
    return render(request, 'index.html', context)
