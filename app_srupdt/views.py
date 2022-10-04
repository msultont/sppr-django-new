from django.shortcuts import render
from django.http import HttpResponse


def index(request):

    return render(request, "index_srupdt.html")


def uploader(request):

    return render(request, "uploader.html")