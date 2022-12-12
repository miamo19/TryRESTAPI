from .models import Snippet
from .serializers import SnippetSerializer

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET', 'POST'])
def snippet_list2(request, format=None):
    #This condition permit to List all code snippets
    if request.method == "GET":
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        return Response(serializer.data)
    
    #This condition permit to create a new snippet
    elif request.method == "POST":
        serializer = SnippetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def snippet_detail2(request, pk, format=None):
    try:
        snippets = Snippet.objects.get(pk=pk)
    except Snippet.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    #This condition permit to Retrieve a code snippet
    if request.method == "GET":
        serializer = SnippetSerializer(snippets)
        return Response(serializer.data)
    
    #This condition permit to Update a code snippet
    elif request.method == "PUT":
        serializer = SnippetSerializer(snippets, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    #This condition permit to Delete a code snippet
    elif request.method == "DELETE":
        snippets.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
    
