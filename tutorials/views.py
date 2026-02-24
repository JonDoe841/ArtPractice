from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from .forms import TutorialCreateForm, TutorialEditForm
from .models import Tutorial
from categories.models import Category
from django.contrib import messages
from django.db.models import Q

def tutorial_edit(request, pk):
    tutorial = get_object_or_404(Tutorial, pk=pk)
    if request.method == 'POST':
        form = TutorialEditForm(request.POST, instance=tutorial)
        if form.is_valid():
            form.save()
            return redirect('tutorials:details', pk=tutorial.pk)
    else:
        form = TutorialEditForm(instance=tutorial)

    return render(
        request,
        'tutorials/tutorial_edit.html',
        {'form': form}
    )


def tutorial_delete(request, pk):
    tutorial = get_object_or_404(Tutorial, pk=pk)

    if request.method == 'POST':
        tutorial.delete()
        messages.success(request, 'Tutorial deleted successfully')
        return redirect('tutorials:tutorial_list')
    return render(request, 'tutorials/tutorial_delete.html', {'tutorial': tutorial})

def tutorial_details(request: HttpRequest, pk: int) -> HttpResponse:
    tutorial = get_object_or_404(Tutorial, pk=pk)
    if not tutorial.is_published:
        return redirect('tutorials:tutorial_list')
    return render(
        request,
        'tutorials/tutorial_details.html',
        {'tutorial': tutorial}
    )

def tutorial_list(request):
    tutorials = Tutorial.published.all()
    query = request.GET.get('q')

    if query:
        tutorials = tutorials.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query)
        )

    paginator = Paginator(tutorials, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'tutorials/tutorial_list.html', {
        'page_obj': page_obj,
        'query': query,
    })

def create_tutorial(request):
    if request.method == 'POST':
        form = TutorialCreateForm(request.POST)
        if form.is_valid():
            tutorial = form.save(commit=False)
            tutorial.is_published = True
            tutorial.save()
            form.save_m2m()
            messages.success(request, "Tutorial created successfully!")
            return redirect('tutorials:tutorial_list')
    else:
        form = TutorialCreateForm()

    return render(request, 'tutorials/tutorial_create.html', {'form': form})

def tutorials_by_category(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    tutorials = Tutorial.published.filter(category=category)

    paginator = Paginator(tutorials, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        'tutorials/tutorial_list.html',
        {
            'page_obj': page_obj,
            'selected_category': category,
            'query': request.GET.get('q', '')
        }
    )
