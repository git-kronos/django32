from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .forms import RecipeForm, RecipeIngredientForm
from .models import Recipe


# Create your views here.
@login_required
def recipe_list_view(request, id=None):
    qs = Recipe.objects.filter(user=request.user)
    context = {
        'object_list': qs
    }
    return render(request, 'recipes/list.html', context)


@login_required
def recipe_detail_view(request, id=None):
    obj = get_object_or_404(Recipe, user=request.user, id=id)
    context = {
        'object': obj
    }
    return render(request, 'recipes/detail.html', context)


@login_required
def recipe_create_view(request, id=None):
    form = RecipeForm(request.POST or None)
    context = {
        'form': form
    }
    if form.is_valid():
        obj = form.save(commit=False)
        obj.user = request.user
        obj.save()
        return redirect(obj.get_absolute_url())
    return render(request, 'recipes/create-update.html', context)


@login_required
def recipe_update_view(request, id=None):
    obj = get_object_or_404(Recipe, user=request.user, id=id)
    form = RecipeForm(request.POST or None, instance=obj)
    form_2 = RecipeIngredientForm(request.POST or None)
    context = {
        'form': form,
        'form_2': form_2,
        'object': obj,
    }
    if all([form.is_valid(), form_2.is_valid()]):
        parent = form.save(commit=False)
        parent.save()
        child = form_2.save(commit=False)
        child.recipe = parent
        child.save()
        print("form", form.cleaned_data)
        print("form_2", form_2.cleaned_data)
        context['message'] = "Data Saved"
    return render(request, 'recipes/create-update.html', context)
