from django.shortcuts import render
from django.http import JsonResponse
from .logic import checkjquery

def jquerycheckView(request):
    if request.method == "GET":
        url=request.GET.get('url', '')
        getversion=request.GET.get('getversion', '')
        verbose=request.GET.get('verbose', '')
        return JsonResponse( checkjquery(url,getversion,verbose))
    else:
        data = {'success' : 'False'}
        return JsonResponse(data)
