from articles.models import Article
from django.shortcuts import render


# Create your views here.
def home_view(request):
    article_queryset = Article.objects.all()
    context = {
        'object_list': article_queryset,
    }
    return render(request, 'home.html', context)
