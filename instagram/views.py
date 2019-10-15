from django.shortcuts import render
from django.http  import HttpResponse,HttpResponseRedirect
from .models import Image, Profile,Instagram
from .forms import InstagramForm
from .email import send_welcome_email
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

def news_today(request):
    if request.method == 'POST':
        form = InstagramForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['your_name']
            email = form.cleaned_data['email']

            recipient = Instagram(name = name,email =email)
            recipient.save()
            send_welcome_email(name,email)

            HttpResponseRedirect('image')
            #.................
    return render(request, 'instas/image.html', {"images":images,"letterForm":form})