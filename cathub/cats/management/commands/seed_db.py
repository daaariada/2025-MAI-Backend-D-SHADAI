import os
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from cats.models import Category, CatImage, UserProfile
from django.conf import settings

class Command(BaseCommand):
    help = 'Creates initial test data'

    def handle(self, *args, **options):
        # есть ли картинка
        image_path = 'cats/whiskers.jpg'
        full_path = os.path.join(settings.MEDIA_ROOT, image_path)
        
        if not os.path.exists(full_path):
            self.stdout.write(self.style.ERROR(f'Image not found at {full_path}'))
            return

        # минус старые данные
        UserProfile.objects.all().delete()
        CatImage.objects.all().delete()
        Category.objects.all().delete()
        User.objects.filter(username='cat_lover').delete()

        # 1 юзер 2 категории 1 картинка
        try:
            user = User.objects.create_user(
                username='cat_lover',
                email='meow@example.com',
                password='password'
            )
            
            profile = UserProfile.objects.create(
                user=user,
                bio='I love cats!'
            )
            
            category1 = Category.objects.create(name='Funny')
            category2 = Category.objects.create(name='Sleeping')
            
            image = CatImage.objects.create(
                title='My Cat',
                uploaded_by=user,
                image=image_path
            )
            image.categories.add(category1, category2)
            
            self.stdout.write(self.style.SUCCESS('Successfully created test data!'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error: {str(e)}'))