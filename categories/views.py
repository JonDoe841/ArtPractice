from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db import models
from tutorials.models import Tutorial
from .models import Category
from .forms import CategoryForm

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'categories/category_list.html', {
        'categories': categories
    })

def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.save(commit=False)
            last_order = Category.objects.aggregate(models.Max('order'))['order__max']
            category.order = (last_order or 0) + 1
            category.save()
            messages.success(request, 'Category added successfully')
            return redirect('categories:category_list')
    else:
        form = CategoryForm()

    return render(request, 'categories/add_category.html', {'form': form})


def category_detail(request, pk):
    category = get_object_or_404(Category, pk=pk)
    tutorials = Tutorial.published.filter(category=category)
    return render(request, 'categories/category_detail.html', {
        'category': category,
        'tutorials': tutorials
    })


def category_edit(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            messages.success(request, 'Category updated')
            return redirect('categories:detail', pk=category.pk)
    else:
        form = CategoryForm(instance=category)

    return render(request, 'categories/category_edit.html', {'form': form, 'category': category})

def category_delete(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        category.delete()
        messages.success(request, 'Category deleted')
        return redirect('categories:category_list')

    return render(request, 'categories/category_delete.html', {'category': category})