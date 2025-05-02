from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.profile_stub, name='profile_api'),
    path('cats/', views.cat_list_stub, name='cats_api'),
    path('categories/', views.categories_stub, name='categories_api'),
]