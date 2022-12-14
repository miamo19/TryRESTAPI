from urllib import response



from snippets.models import Snippet
from snippets.serializers import SnippetSerializer

from django.http import Http404

from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

#       +++++classBased APIView++++++
class SnippetList(APIView):
    """ 
    name: SnippetList
    description : This class permit to list all code snippet and to create a code snippet with the different method get and post
    """
    
    #This method permit to list all the code snippets 
    def get(self, request, format=None):
        snippet = Snippet.objects.all()
        serializer = SnippetSerializer(snippet, many=True)
        return Response(serializer.data)
    
    #This method permit to create (post) a code snippet
    def post(self, request, format=None):
        serializer = SnippetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
#create a name variable for the class to be use in urls.py
snippet_view_list = SnippetList.as_view()
    
class SnippetDetail(APIView):
     """ 
    name: SnippetDetail
    description : This class permit to retrieve, update and delete a code snippet using different methods
    """
    
    def get_object(self, pk):
        try:
            return Snippet.objects.get(pk=pk)
        except Snippet.DoesNotExist:
            raise Http404
    
    #This method permit to retrieve a code snippet
    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = SnippetSerializer(snippet)
        return Response(serializer.data)
    
    #This method permit to Update a code snippet
    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = SnippetSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    #This mehtod permit to delete (destroy) a code snippet
    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

snippet_view_detail = SnippetDetail.as_view()

    
        
    
    
