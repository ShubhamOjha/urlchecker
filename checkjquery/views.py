from django.shortcuts import render
from django.http import JsonResponse
from .logic import checkjquery

def jquerycheckView(request):
    if request.is_ajax() and request.method == "GET":
        url=str(request.GET.get('url', ''))
        getversion=str(request.GET.get('getversion', ''))
        verbose=str(request.GET.get('verbose', ''))
        return JsonResponse( checkjquery(url,getversion,verbose))
    else:
        data = {'success' : 'False'}
        return JsonResponse(data)
