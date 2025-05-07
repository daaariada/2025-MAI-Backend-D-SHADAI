from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.profile_stub, name='profile_api'),
    path('search/', views.search_cats, name='search_cats'),
    path('cats/', views.cat_list, name='cats_list'),
    path('cats/create/', views.create_cat, name='create_cat'),
    path('categories/', views.categories_stub, name='categories_api'),
]