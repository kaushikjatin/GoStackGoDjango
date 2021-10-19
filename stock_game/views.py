from django.shortcuts import render
from django.http import JsonResponse, HttpResponse


def rules(request):
    apple_1 = request.GET['apple_1']
    apple_2 = request.GET['apple_2']

    data = {
        "name": 'heloo',
        "age": 23
    }pi
    return JsonResponse(data)
