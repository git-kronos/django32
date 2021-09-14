from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404, Http404
from django.urls import reverse
from django.forms.models import modelformset_factory
from .forms import RecipeForm, RecipeIngredientForm
from .models import Recipe, RecipeIngredient


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
def recipe_delete_view(request, id=None):
    obj = get_object_or_404(Recipe, user=request.user, id=id)
    if request.method == "POST":
        obj.delete()
        success_url = reverse('recipes:list')
        return redirect(success_url)
    context = {
        'object': obj
    }
    return render(request, 'recipes/delete.html', context)


@login_required
def recipe_detail_hx_view(request, id=None):
    if not request.htmx:
        raise Http404
    try:
        obj = Recipe.objects.get(id=id, user=request.user)
    except Exception as e:
        obj = None
    if obj is None:
        return HttpResponse("Not Found")
    context = {
        'object': obj
    }
    return render(request, 'recipes/partials/detail.html', context)


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
        if request.htmx:
            headers={
                'HX-Redirect':obj.get_absolute_url()
            }
            return HttpResponse("Created", headers=headers)
        return redirect(obj.get_absolute_url())
    return render(request, 'recipes/create-update.html', context)


@login_required
def recipe_update_view(request, id=None):
    obj = get_object_or_404(Recipe, user=request.user, id=id)
    form = RecipeForm(request.POST or None, instance=obj)
    new_ingredient_url = reverse('recipes:hx-ingredient-create', kwargs={'parent_id': obj.id})

    context = {
        'form': form,
        'object': obj,
        'new_ingredient_url': new_ingredient_url
    }
    if form.is_valid():
        form.save()
        context['message'] = "Data Saved"
    if request.htmx:
        return render(request, 'recipes/partials/forms.html', context)
    return render(request, 'recipes/create-update.html', context)


@login_required
def recipe_ingredient_update_hx_view(request, id=None, parent_id=None):
    if not request.htmx:
        raise Http404
    try:
        parent_obj = Recipe.objects.get(id=parent_id, user=request.user)
    except Exception as e:
        parent_obj = None
    if parent_obj is None:
        return HttpResponse("Not Found")
    instance = None
    if id is not None:
        try:
            instance = RecipeIngredient.objects.get(recipe=parent_obj, id=id)
        except:
            instance = None
    form = RecipeIngredientForm(request.POST or None, instance=instance)
    url = instance.get_hx_edit_url() if instance else reverse('recipes:hx-ingredient-create',
                                                              kwargs={'parent_id': parent_obj.id})
    context = {
        'url': url,
        'object': instance,
        'form': form
    }
    if form.is_valid():
        new_obj = form.save(commit=False)
        if instance is None:
            new_obj.recipe = parent_obj
        new_obj.save()
        context['object'] = new_obj
        return render(request, 'recipes/partials/ingredient-inline.html', context)
    return render(request, 'recipes/partials/ingredient-form.html', context)


@login_required
def recipe_ingredient_delete_view(request, parent_id=None, id=None):
    obj = get_object_or_404(
        RecipeIngredient,
        recipe__id=parent_id,
        id=id,
        recipe__user=request.user,
    )
    if request.method == "POST":
        obj.delete()
        success_url = reverse('recipes:detail', kwargs={'id': parent_id})
        return redirect(success_url)
    context = {
        'object': obj
    }
    return render(request, 'recipes/delete.html', context)
