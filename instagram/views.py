from django.shortcuts import render
from django.http  import HttpResponse,HttpResponseRedirect
from .models import Image, Profile,Instagram
from .forms import InstagramForm
# Create your views here.

def image(request):
    images = Image.objects.all()

    if request.method == 'POST':
        form = InstagramForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['your_name']
            email = form.cleaned_data['email']
            recipient = Instagram(name = name,email =email)
            recipient.save()
            HttpResponseRedirect('image')
    else:
        form = InstagramForm()
    return render(request, 'instas/image.html', {"images":images,"letterForm":form})