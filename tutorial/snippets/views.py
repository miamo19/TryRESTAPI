from snippets.models import Snippet
from snippets.serializers import SnippetSerializer

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import  JSONParser

    #+++++++++Regular Django views+++++++++++
    
#List all code snippets, or create a new snippet.@csrf_exempt
@csrf_exempt
def snippet_list(request):
 
    #List all code snippets.   
    if request.method == 'GET':
        snippet     = Snippet.objects.all()
        serializer  = SnippetSerializer(snippet, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    #create a new snippet.
    elif request.method == 'POST':
        data        = JSONParser().parse(request)
        serializer  = SnippetSerializer(data=data)
        if serializer.is_valid():
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt  
def snippet_detail(request, pk):
    try:
        snippet = Snippet.objects.get(pk=pk)
    except Snippet.DoesNotExist:
        return HttpResponse(status=404)
    
    #Retrieve
    if request.method == 'GET':
        serializer = SnippetSerializer(snippet)
        return JsonResponse(serializer.data, safe=False)
    
    #Update
    elif request.method == "PUT":
        data = JSONParser().parse(request)
        serializer = SnippetSerializer(snippet, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
        
    #Delete
    elif request.method == "DELETE":
        snippet.delete()
        return HttpResponse(status=204)
    
    
    

    
