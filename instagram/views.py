from django.shortcuts import render
from django.http  import HttpResponse,HttpResponseRedirect
from .models import Image, Profile,Instagram
from .forms import InstagramForm
from .email import send_welcome_email
from django.contrib.auth.decorators import login_required
# Create your views here.



@login_required(login_url='/accounts/login/')
def image(request):
    images = Image.objects.all()
    form = InstagramForm(request.POST)
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
    return render(request, 'instas/image.html', {'letterForm':form,"images":images})

def search_results(request):
        pass