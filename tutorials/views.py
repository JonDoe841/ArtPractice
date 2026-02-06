from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

def tutorial_add(request: HttpRequest) -> HttpResponse:
    return render(request, 'tutorials/tutorial_add.html')

def tutorial_edit(request: HttpRequest, pk: int) -> HttpResponse:
    return render(request, 'tutorials/tutorial_edit.html')

def tutorial_delete(request: HttpRequest, pk: int) -> HttpResponse:
    return render(request, 'tutorials/tutorial_delete.html')

def tutorial_details(request: HttpRequest, pk: int) -> HttpResponse:
    return render(request, 'tutorials/tutorial_details.html')
def tutorial_list(request: HttpRequest) -> HttpResponse:
    return render(request, 'tutorials/tutorial_list.html')