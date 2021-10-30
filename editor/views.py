from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from .models import Document, Chapter, Section
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required
def index(request):
    uname = str(request.user)
    request.session['user_name'] = uname

    documents = Document.objects.all()

    if request.method == "POST":

        file_name = request.POST.get('file_name')

        d = Document(title=file_name)
        d.save()

        return redirect(f'{d.document_id}/')
    return render(request, 'index.html', {"documents": documents, "user_name": uname})


@login_required
def editor_view(request, file_id):
    doc = Document.objects.get(document_id=file_id)
    chapters = Chapter.objects.filter(document=doc)
    sections = {}
    for chapter in chapters:
        sec = Section.objects.filter(chapter=chapter)
        sections[chapter] = sec
    return render(request, 'editor_view.html', {'document': doc, 'chapters': chapters, 'sections': sections})


def section_view(request, file_id, slug):
    #doc = Document.objects.get(document_id=file_id)
    section = Section.objects.get(slug=slug)

    if request.method == "POST":
        print(request.POST)
        section.title = request.POST.get('section_name')
        section.content = request.POST.get('content')
        section.save()


    context = {'section': section}
    return render(request, 'section_view.html', context)


def chapter_view(request, file_id, slug):
    doc = Document.objects.get(document_id=file_id)
    chapter = Chapter.objects.get(document=doc, slug=slug)

    context = {'chapter': chapter}

    return render(request, 'chapter_view.html', context)
