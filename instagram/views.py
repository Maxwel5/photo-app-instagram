from django.shortcuts import render, redirect
from django.http  import HttpResponse,HttpResponseRedirect
from .models import Image, Profile,Instagram
from .forms import UserRegisterForm
from .email import send_welcome_email
from django.contrib.auth.decorators import login_required
# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
        return redirect('login')

    else:
       form = UserRegisterForm()
    return render(request, 'registration/registration_form.html', {'form':form})




def image(request):
    image = image()
    image.name = 'Food'
    image.profile = 'mash.jpeg'
    image.like_count = 12
    
    return render(request, 'instas/image.html', {'image':image})

def search_results(request):
    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_images = Image.search_by_name(search_term)
        message = f"{search_term}"

        return render(request, 'instas/search.html',{"message":message,"images": searched_images})

    else:
        message = "Nothing has been searched"
        return render(request, 'instas/search.html',{"message":message})
        pass

@login_required
def index(request):
    images = Image.objects.all()
    context={
        'images':images
    }
    return render(request,'instas/index.html',context)

