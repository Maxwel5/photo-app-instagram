from django.shortcuts import render
from django.http  import HttpResponse

# Create your views here.
# def instagram(request):
#     return render(request,'instagram.html')

def image(request):
    image = Image.objects.all()
    return render(request, instas/image.html)