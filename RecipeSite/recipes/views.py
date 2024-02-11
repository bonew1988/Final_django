# recipes/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .forms import RecipeForm
from .models import Recipe
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout
from django.shortcuts import redirect


def home(request):
    recipes = Recipe.objects.order_by('?')[:5]
    return render(request, 'recipes/home.html', {'recipes': recipes})


def recipe_edit(request, pk=None):
    if pk:
        recipe = get_object_or_404(Recipe, pk=pk)
    else:
        recipe = None

    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES, instance=recipe)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.author = request.user
            recipe.save()
            print("Recipe saved successfully!")
            return redirect('recipe_detail', pk=recipe.pk)
        else:
            print("Form is not valid:", form.errors)
    else:
        form = RecipeForm(instance=recipe)

    return render(request, 'recipes/recipe_edit.html', {'form': form, 'recipe': recipe})


# recipes/views.py


def recipe_home(request):
    recipes = Recipe.objects.order_by('?')[:5]
    groups = Recipe.objects.values('group').distinct()

    return render(request, 'recipes/home.html', {'recipes': recipes, 'groups': groups})


def recipe_list(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipes/recipe_list.html', {'recipes': recipes})


def recipe_detail(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    return render(request, 'recipes/recipe_detail.html', {'recipe': recipe})


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('home')
