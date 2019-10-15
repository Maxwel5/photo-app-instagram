from django.shortcuts import render
from django.http  import HttpResponse
from .models import Image, Profile
# Create your views here.

def image(request):
    images = Image.objects.all()
    return render(request, 'instas/image.html', {"images":images})