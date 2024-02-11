# recipes/urls.py
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('edit/<int:pk>/', views.recipe_edit, name='recipe_edit'),
    path('list/', views.recipe_list, name='recipe_list'),
    path('detail/<int:pk>/', views.recipe_detail, name='recipe_detail'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('add/', views.recipe_edit, name='recipe_add'),  # Добавленный URL-путь
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
