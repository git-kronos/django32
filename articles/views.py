from django.shortcuts import render
from django.contrib.auth.decorators import login_required

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
        object = form.save()
        # title = form.cleaned_data.get('title')
        # content = form.cleaned_data.get('content')

        # object = Article.objects.create(title=title, content=content)
        context['object'] = ArticleForm()
        # context['object'] = object
        context['created'] = True

    return render(request, 'article/create.html', context)


def article_detail_view(request, id):
    object = Article.objects.get(id=id)
    context = {
        "object": object,
    }
    return render(request, 'article/detail.html', context)
