from django.http import HttpResponse, HttpRequest
from django.shortcuts import render

def add_category(request: HttpRequest)-> HttpResponse:
    return render(request, 'categories/add_category.html')

def category_detail(request: HttpRequest, category_id: int) -> HttpResponse:
    return render(request, 'categories/category_detail.html')

def category_list(request: HttpRequest) -> HttpResponse:
    return render(request, 'categories/category_list.html')

def category_edit(request: HttpRequest, category_id: int) -> HttpResponse:
    return render(request, 'categories/category_edit.html')

def category_delete(request: HttpRequest, category_id: int) -> HttpResponse:
    return render(request, 'categories/category_delete.html')

