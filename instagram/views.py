from django.shortcuts import render
from django.http  import HttpResponse
# Create your views here.

def image(request):
    return render(request, 'instas/image.html')