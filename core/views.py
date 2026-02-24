from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from tutorials.models import Tutorial

def home_page(request: HttpRequest) -> HttpResponse:
    latest_tutorials = Tutorial.published.all().order_by('-created_at')[:5]
    return render(request, 'core/home_page.html', {
        'tutorials': latest_tutorials
    })