from django.http import JsonResponse
from django.shortcuts import render


# Create your views here.
def zuri_api(request):
    return JsonResponse(
        {
            "slackUsername": "patience izere", 
            "backend": True,
            "age": 21,
            "bio": "Motivated, high ambitious and hard working person fitting into world technology based era"
        }
    )
