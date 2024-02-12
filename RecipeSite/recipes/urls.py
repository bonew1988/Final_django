# recipes/urls.py
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
from .views import recipe_list, recipe_detail, recipe_edit
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('', views.home, name='home'),
    path('edit/<int:pk>/', views.recipe_edit, name='recipe_edit'),
    path('list/', views.recipe_list, name='recipe_list'),
    path('detail/<int:pk>/', views.recipe_detail, name='recipe_detail'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('add/', views.recipe_edit, name='recipe_add'),
    path('recipe/<int:pk>/', recipe_detail, name='recipe_detail'),
    path('login/', LoginView.as_view(), name='login'),
    path('recipe/<int:pk>/edit/', recipe_edit, name='recipe_edit')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



