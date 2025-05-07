from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q
from .models import CatImage
from django.contrib.auth.models import User

# профиль
@require_http_methods(["GET"])
def profile_stub(request):
    return JsonResponse({"message": "Profile API stub"})

# картинки
@csrf_exempt
@require_http_methods(["POST"])
def create_cat(request):
    try:
        title = request.POST.get('title')
        image = request.FILES.get('image')
        username = request.POST.get('username')
        
        if not all([title, image, username]):
            return JsonResponse({'error': 'Missing data (need title, image AND username)'}, status=400)
        
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return JsonResponse({'error': f'User {username} not found'}, status=404)
            
        cat = CatImage.objects.create(
            title=title,
            image=image,
            uploaded_by=user
        )
        return JsonResponse({'id': cat.id}, status=201)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

@require_http_methods(["GET"])
def cat_list(request):
    cats = CatImage.objects.all().values('id', 'title', 'image')
    return JsonResponse(list(cats), safe=False)
    
@require_http_methods(["GET"])
def search_cats(request):
    query = request.GET.get('q', '')
    if query:
        results = CatImage.objects.filter(
            Q(title__icontains=query) | 
            Q(uploaded_by__username__icontains=query)
        ).values('id', 'title', 'image')
        return JsonResponse(list(results), safe=False)
    return JsonResponse([], safe=False)

# категории
@require_http_methods(["GET"])
def categories_stub(request):
    return JsonResponse({"message": "Categories API stub"})
