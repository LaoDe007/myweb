from django.shortcuts import render, HttpResponse, redirect
from django import forms


def login(request):
    return render(request, "layout.html")