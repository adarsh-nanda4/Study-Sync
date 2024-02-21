from django.shortcuts import render


def home(request):
    return render(request,'home.html')

def tryy(request):
    return render(request,'try.html')

def add(request):
    return render(request,'add.html')