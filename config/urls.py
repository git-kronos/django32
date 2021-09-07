from django.contrib import admin
from django.urls import path, include
from accounts import views as accounts
from articles import views as articles
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('pantry/', include('recipes.urls'), name='recipes'),
    path('articles/', include('articles.urls'), name='articles'),
    path('register/', accounts.register_view, name='register'),
    path('login/', accounts.login_view, name='login'),
    path('logout/', accounts.logout_view, name='logout'),
    path('admin/', admin.site.urls),
]
