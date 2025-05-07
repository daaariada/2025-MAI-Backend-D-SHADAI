from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    
    class Meta:
        verbose_name_plural = "Categories"  # чтобы не было Categorys

    def __str__(self):
        return self.name

class CatImage(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='cats/')
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE) # ForeignKey - у картинки один пользователь, у пользователя много картинок
    categories = models.ManyToManyField(Category) # ManyToMany - одна картинка = много категорий, у категорий много картинок
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # OneToOne - один пользователь один профиль
    bio = models.TextField(blank=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True)
    
    def __str__(self):
        return f"{self.user.username}'s profile"
