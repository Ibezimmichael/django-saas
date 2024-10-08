import pathlib
from django.http import HttpResponse
from django.shortcuts import render
from visits.models import PageVisit

this_dir = pathlib.Path(__file__).resolve().parent


def home(request, *args, **kwargs):
    queryset = PageVisit.objects.filter(path=request.path)
    my_title = "Michael"
    my_context = {
        "page_title": my_title,
        "visits": queryset   
    }
    html_template = "home.html"
    PageVisit.objects.create(path=request.path)
    return render(request, html_template, my_context)