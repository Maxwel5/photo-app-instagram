from django.shortcuts import render
from django.http  import HttpResponse

# Create your views here.
def instagram(request):
    # return HttpResponse('Instagram App')
    return render(request,'instagram.html')

def image(request):
    # image = 
    return render(request, instas/image.html)