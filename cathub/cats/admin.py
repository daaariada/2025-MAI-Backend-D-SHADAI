from django.contrib import admin
from .models import Category, CatImage, UserProfile

admin.site.register(Category)
admin.site.register(CatImage)
admin.site.register(UserProfile)