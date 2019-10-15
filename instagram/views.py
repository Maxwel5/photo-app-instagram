from django.shortcuts import render
from django.http  import HttpResponse
from .models import Image, Profile
from .forms import InstagramForm
# Create your views here.

def image(request):
    images = Image.objects.all()

    if request.method == 'POST':
        form = InstagramForm(request.POST)
        if form.is_valid():
            print('valid')
    else:
        form = InstagramForm()
    return render(request, 'instas/image.html', {"images":images,"letterForm":form})