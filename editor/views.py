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

        d = Document(name=file_name)
        d.save()

        return redirect(f'{d.document_id}/')
    return render(request, 'index.html', {"documents": documents, "user_name": uname})


@login_required
def editor_view(request, file_id):
    context = {}
    doc = Document.objects.get(document_id=file_id)
    
    if request.method == "POST":
        title = request.POST['title1']
        content = request.POST['content1']
        chapter = Chapter(document=doc, title="Literature Survey", order=1)
        chapter.save()
        section = Section(chapter=chapter, title=title,
                          content=content, order=1)
        section.save()
        context = {'title1': title}

    if Section.objects.filter(title="xyz").exists():
        section = Section.objects.get(title="xyz")
        context['content1'] = section.content
        print(section.pk)
    return render(request, 'editor_view.html', context)
