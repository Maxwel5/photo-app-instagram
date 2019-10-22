from django.shortcuts import render, redirect,get_object_or_404
from django.http  import HttpResponse,HttpResponseRedirect
from .models import Image, Profile,Instagram
from .forms import UserRegisterForm,CommentForm
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
    
    return render(request, 'instas/image.html')

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
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            # comment.image = post
            comment.save()
            return redirect('index')
    else:
        form = CommentForm()
    context={
        'images':images,
        'form': form
    }
    return render(request,'instas/index.html',context)

@login_required(login_url='/register/')
def likePost(request,image_id):

        image = Image.objects.get(pk = image_id)

        if image.likes.filter(id = request.user.id).exists():
            image.likes.remove(request.user)
            is_liked = False
        else:
            image.likes.add(request.user)
            is_liked = True

        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@login_required(login_url='/register/')
def add_comment_to_post(request, pk):
    # post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            # comment.image = post
            comment.save()
            return redirect('index')
    else:
        form = CommentForm()
    return render(request, 'instas/post_detail.html', {'form': form})



