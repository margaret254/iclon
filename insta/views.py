from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404,HttpResponseRedirect
import datetime as dt
from .models import Post
from .forms import PostForm
from .email import send_welcome_email
from django.contrib.auth.decorators import login_required
# Create your views here.



@login_required(login_url='/accounts/register/')
def new_post(request):
    date = dt.date.today()
    posts = Post.objects.all()
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            caption = form.cleaned_data['caption']
            image = form.cleaned_data['Upload image']
            recipient = PostRecipients(caption = caption,image=image)
            recipient.save()
            send_welcome_email(caption,image)
            HttpResponseRedirect('newpost')
            print('valid')
    else:
        form = PostForm()
    return render(request, 'all-insta/post.html', {"date": date,'posts': posts,"postForm":form})

def search_results(request):
    if 'post' in request.GET and request.GET["post"]:
        search_term = request.GET.get("post")
        searched_posts = Post.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'all-insta/search.html',{"message":message,"posts": searched_posts})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-insta/search.html',{"message":message})

@login_required(login_url='/accounts/login/')
def post(request):

    try:
        post = Post.objects.get(id = post_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"all-insta/single_post.html", {"post":post})
    

@login_required(login_url='/accounts/login/')
def profile(request):
    current_user = request.user
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.profile = current_user
            post.save()
        return redirect('newpost')

    else:
        form = PostForm()
    return render(request, 'profile.html', {"form": form})
