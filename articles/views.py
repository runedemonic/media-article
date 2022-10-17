import os

from django.shortcuts import render, redirect
from articles.forms import ArticleForm
# Create your views here.
from articles.models import Article


def create(request):
    if request.method == 'POST':
        article_form = ArticleForm(request.POST)
        if article_form.is_valid():
            title = request.POST['title']
            content = request.POST['content']
            img = request.FILES['img']
            thumbnail = request.FILES['thumbnail']
            data = Article(
                title=title,
                content=content,
                img=img,
                thumbnail=thumbnail,
            )
            data.save()
        return redirect('articles:index')
    else:
        article_form = ArticleForm()
    context = {
        'article_form': article_form
    }
    return render(request, 'articles/create.html', context=context)


def detail(request, _pk):
    data = Article.objects.get(pk=_pk)
    context = {
        "data": data,
    }
    return render(request, "articles/detail.html", context)


def index(request):
    data = Article.objects.all()
    context = {
        "data": data,
    }
    return render(request, "articles/index.html", context)


def update(request,_pk):
    temp = Article.objects.get(pk=_pk)
    article_form = ArticleForm(request.POST or None, request.FILES or None, instance=temp)
    if article_form.is_valid():
        if temp.image:
            os.remove(temp.image.path)
        if temp.thumbnail:
            os.remove(temp.thumbnail.path)
        article_form.save()
        return redirect('articles:detail',_pk)
    context = {
        'article_form': article_form,
    }
    return render(request, 'articles/create.html', context)


def delete(request,_pk):
    temp = Article.objects.get(pk=_pk)
    if temp.img:
        os.remove(temp.img.path)
    if temp.thumbnail:
        os.remove(temp.thumbnail.path)
    temp.delete()
    return redirect('articles:index')