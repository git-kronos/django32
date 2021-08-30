from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from django.http import Http404
from .forms import ArticleForm
from .models import Article


def article_search_view(request):
    try:
        query = int(request.GET.get('q'))
    except Exception as e:
        query = None

    article_obj = None
    if query is not None:
        article_obj = Article.objects.get(id=query)

    context = {
        'object': article_obj
    }
    return render(request, 'article/search.html', context)


# @login_required
# def article_create_view(request):
#     context = {
#         'form': ArticleForm()
#     }
#     if request.method == "POST":
#         form = ArticleForm(request.POST)
#         context['form'] = form
#         if form.is_valid():
#             title = form.cleaned_data.get('title')
#             content = form.cleaned_data.get('content')

#             object = Article.objects.create(title=title, content=content)
#             context['object'] = object
#             context['created'] = True

#     return render(request, 'article/create.html', context)


@login_required
def article_create_view(request):
    form = ArticleForm(request.POST or None)
    context = {
        'form': form
    }
    if form.is_valid():
        article_object = form.save()
        context['form'] = ArticleForm()
        return redirect(article_object.get_absolute_url())

    return render(request, 'article/create.html', context)


def article_detail_view(request, slug):
    article_obj=None
    if slug is not None:
        try:
            article_obj = Article.objects.get(slug=slug)
        except Article.DoesNotExist:
            raise Http404
        except Article.MultipleObjectsReturned:
            article_obj = Article.objects.filter(slug=slug).first()
        except:
            raise Http404

    context = {
        "object": article_obj,
    }
    return render(request, 'article/detail.html', context)
