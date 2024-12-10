from django.shortcuts import render, get_object_or_404, redirect
from .models import Document
from .forms import DocumentForm

def document_list(request):
    documents = Document.objects.all()
    return render(request, 'jinja2/documents/document_list.html', {'documents': documents})

def document_create(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('document_list')
    else:
        form = DocumentForm()
    return render(request, 'jinja2/documents/document_form.html', {'form': form})

def document_edit(request, pk):
    document = get_object_or_404(Document, pk=pk)
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES, instance=document)
        if form.is_valid():
            form.save()
            return redirect('document_list')
    else:
        form = DocumentForm(instance=document)
    return render(request, 'jinja2/documents/document_form.html', {'form': form})

def document_delete(request, pk):
    document = get_object_or_404(Document, pk=pk)
    if request.method == 'POST':
        document.delete()
        return redirect('document_list')
    return render(request, 'jinja2/documents/document_confirm_delete.html', {'document': document})

def document_detail(request, pk):
    document = get_object_or_404(Document, pk=pk)
    return render(request, 'jinja2/documents/document_detail.html', {'document': document})