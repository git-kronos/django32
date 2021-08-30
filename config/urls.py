from django.contrib import admin
from django.urls import path, include
from accounts import views as accounts
from articles import views as articles
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),

    path('articles/', articles.article_search_view),
    path('articles/create/', articles.article_create_view, name='article-create'),
    path('articles/<slug:slug>/', articles.article_detail_view, name='article-detail'),

    path('register/', accounts.register_view, name='register'),
    path('login/', accounts.login_view, name='login'),
    path('logout/', accounts.logout_view, name='logout'),

    path('admin/', admin.site.urls),
]
