from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def mtcnn(request):
    return render(request, 'mtcnn.html')

def tiny(request):
    return render(request, 'tiny.html')

def ssd(request):
    return render(request, 'mobilenet.html')
