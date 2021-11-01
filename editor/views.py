from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.utils.text import slugify
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

    # if request.method == "POST":
    #     if request.POST.get("add_chapter"):
    #         print("Chapter added")
    #     elif request.POST.get("add_section"):
    #         chapter_title = request.POST.get("chapter_title")
    #         print(chapter_title)
    #         chapter = Chapter.objects.get(title=chapter_title, document=doc)
    #         if Section.objects.filter(chapter=chapter, title="New Section").exists():
    #             print("Already exists")
    #         else:
    #         section = Section(chapter=chapter)
    #         section.save()
    #         print(section.slug)
    #         redirect("section_view", file_id=file_id, chapter_slug=chapter.slug, section_slug=section.slug)

    if Chapter.objects.filter(document=doc).exists():

        chapters = Chapter.objects.filter(document=doc)
        sections = {}
        for chapter in chapters:
            sec = Section.objects.filter(chapter=chapter)
            sections[chapter] = sec

        context = {'document': doc, 'chapters': chapters, 'sections': sections}
    else:
        context = {}
    return render(request, 'editor_view.html', context)


def section_view(request, file_id, chapter_slug, section_slug):
    doc = Document.objects.get(document_id=file_id)
    chapter = Chapter.objects.get(document=doc, slug=chapter_slug)
    section = Section.objects.get(chapter=chapter, slug=section_slug)

    if request.method == "POST":
        section_title = request.POST.get('section_name')
        if Section.objects.filter(chapter=chapter, title=section_title).exists():
            section.content = request.POST.get('content')
            section.save()
        else:
            section.title = request.POST.get('section_name')
            section.content = request.POST.get('content')
            section.save()

            return redirect("section_view", file_id=file_id,
                            chapter_slug=chapter_slug, section_slug=section.slug)

    context = {'chapter': chapter, 'section': section}
    return render(request, 'section_view.html', context)


def chapter_view(request, file_id, slug):
    doc = Document.objects.get(document_id=file_id)
    chapter = Chapter.objects.get(document=doc, slug=slug)

    context = {'chapter': chapter}

    return render(request, 'chapter_view.html', context)


def new_section_view(request, file_id, chapter_slug):
    doc = Document.objects.get(document_id=file_id)
    chapter = Chapter.objects.get(document=doc, slug=chapter_slug)

    if request.method == "POST":
        section_title = request.POST.get('section_name')
        section_content = request.POST.get('content')

        if Section.objects.filter(chapter=chapter, title=section_title).exists():
            print("Already exists")
        else:
            section = Section(
                chapter=chapter, title=section_title, content=section_content)
            section.save()
            return redirect("section_view", file_id=file_id,
                            chapter_slug=chapter_slug, section_slug=section.slug)

    #context = {'section': section}
    return render(request, 'section_view.html')
