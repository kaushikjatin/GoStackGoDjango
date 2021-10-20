from django.shortcuts import render
from django.http import JsonResponse, HttpResponse, HttpRequest

google = {"m1": 1341.550049, "m2": 1462}
facebook = {"m1": 206.75, "m2": 203.440002}
amazon = {"m1": 1875, "m2": 2010.599976}
apple = {"m1": 74.059998, "m2": 76.074997}


def rules(request):
    if request.method == 'GET':
        apple_1 = request.GET.get("facebook")
        print("Apple : ", apple_1)
        # apple_2 = request.GET.get('facebook')

        data = {
            "name": apple_1,
            "age": 10}
        return JsonResponse(data)
    else:
        return HttpResponse("No post req")
