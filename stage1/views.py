from django.http import JsonResponse
from django.shortcuts import render


# Create your views here.
def zuri_api(request):
    return JsonResponse(
        {
            "slackUsername": "itsweshy", 
            "backend": True,
            "age": 25,
            "bio": "Hooked on continuous self-improvement, open to new exciting opportunities and passionate about the Django backend space"
        }
    )
