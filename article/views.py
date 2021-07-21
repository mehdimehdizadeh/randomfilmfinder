from article.models import Article,Mylist
from django.shortcuts import redirect, render
from .forms import RegisterForm,LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages
from random import randint
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
# Create your views here.

def register(request):
    form = RegisterForm(request.POST or None)
    context = {
        'form':form
    }
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        if User.objects.filter(username = username).first():
            messages.warning(request, 'This username has already been used!')
            return render(request,"register.html",context)
        newUser = User(username = username)
        newUser.set_password(password)
        newUser.save()
        login(request,newUser)
        return redirect('/user/film')
    return render(request,"register.html",context)

def sign(request):
    form = LoginForm(request.POST or None)
    context = {
        'form':form
    }
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username = username,password = password)
        if user is None:
            messages.info(request,"Password is note correct")
            return render(request,"sign.html",context)
        login(request,user)
        return redirect('/user/film')
    return render(request,"sign.html",context)

def list(request):
    posts_list = Mylist.objects.filter(user = request.user)
    paginator = Paginator(posts_list,20)
    page = request.GET.get('page')
    try:
        film = paginator.page(page)
    except PageNotAnInteger:
        film = paginator.page(1)
    except EmptyPage:
        film = paginator.page(paginator.num_pages)
    context = {
        'film':film,
    }
    return render(request,"list.html",context)

def mylist(request,id):
    article = Article.objects.filter(id = id).first()
    filma = Mylist(user = request.user,title = article.title,director = article.director,image = article.image,value = article.value)
    filma.save()
    posts_list = Mylist.objects.filter(user = request.user)
    paginator = Paginator(posts_list,20)
    page = request.GET.get('page')
    try:
        film = paginator.page(page)
    except PageNotAnInteger:
        film = paginator.page(1)
    except EmptyPage:
        film = paginator.page(paginator.num_pages)
    context = {
        "film":film,
    }
    return render(request,"list.html",context)

def film(request):
    mylist = Mylist.objects.filter(user = request.user)
    article_list = Article.objects.all()
    list = []
    mist = []
    for i in mylist:
        mist.append(i.id)
    for i in article_list:
        list.append(i.id)
    while True:
        s = 0
        r = randint(1,len(list))
        if len(list)!=len(mist):
            if len(mist)>0:
                marticle = Article.objects.get(id = r)
                for i in range(len(mist)):
                    value = Mylist.objects.get(user = request.user, id = mist[i])
                    if value.title == marticle.title and value.director == marticle.director:
                        s = s + 1
                if s == 0:
                    article = Article.objects.filter(id = r)
                    context = {
                        'article':article
                    }
                    return render(request,'film.html',context)
                    break
            else:
                article = Article.objects.filter(id = r)
                context = {
                        'article':article
                    }
                return render(request,'film.html',context)
                break
        else:
            return redirect('/user/list')
            break
        
        



def userlogout(request):
    logout(request)
    form = LoginForm(request.POST or None)
    context = {
        'form':form
    }
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username = username,password = password)
        if user is None:
            messages.info(request,"Password is note correct")
            return render(request,"sign.html",context)
        login(request,user)
        return redirect('/user/film')
    return render(request,"sign.html",context)
