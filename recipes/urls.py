from django.urls import path

from . import views

app_name = 'recipes'

urlpatterns = [
    path('', views.recipe_list_view, name="list"),
    path('create/', views.recipe_create_view, name="create"),
    path('hx/<int:id>/', views.recipe_detail_hx_view, name="hx-detail"),
    path('hx/<int:parent_id>/ingredient/<int:id>/', views.recipe_ingredient_update_hx_view, name="hx-ingredient-detail"),
    path('hx/<int:parent_id>/ingredient/', views.recipe_ingredient_update_hx_view, name="hx-ingredient-create"),
    path('<int:id>/edit/', views.recipe_update_view, name="update"),
    path('<int:id>/', views.recipe_detail_view, name="detail"),
]
