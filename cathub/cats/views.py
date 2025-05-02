from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt

@require_http_methods(["GET"])
def profile_stub(request):
    return JsonResponse({"message": "Profile API stub"})

@csrf_exempt
@require_http_methods(["GET", "POST"])
def cat_list_stub(request):
    if request.method == "GET":
        return JsonResponse({"message": "Cats API stub"})
    elif request.method == "POST":
        return JsonResponse({"status": "created"}, status=201)

@require_http_methods(["GET"])
def categories_stub(request):
    return JsonResponse({"message": "Categories API stub"})
