from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.contrib.auth.models import AnonymousUser
from .models import Post
from .forms import PostForm, Contact_form
from django.core.mail import send_mail
from django.http import HttpResponseRedirect

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request,'blog/post_list.html',{'posts':posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            
            if request.user.is_authenticated():
                post.author = request.user
            else:
                post.author = AnonymousUser.get_username()
            post.published_date = timezone.now()
            post.save()
            return redirect('blog.views.post_detail', pk=post.pk)
        else:
            raise form.ValidationError("Error")
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form':form})

def about_us(request):
    return render(request, 'blog/about_us.html')


def contact_form(request):
    if request.method == "POST":
        form = contact_form(request.POST)
        if form.is_valid():
            asunto = form.cleaned_data['asunto']
            mensaje = form.cleaned_data['mensaje']
            emisor = form.cleaned_data['emisor']
            cc = form.cleaned_data['cc']
        
            recipients = ['userdjangocontact@gmail.com']
            if cc:
                recipients.append(emisor)
        
            send_mail(asunto, mensaje, emisor, recipients)
            return HttpResponseRedirect('blog/post_list.html')
    else:
        form = Contact_form
    return render(request, 'blog/contact_form.html', {'form':form})
        