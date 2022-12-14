#from project
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer

#from rest_framework
from rest_framework import mixins
from rest_framework import generics

#        ++++👇👇 Using mixins Classes 👇👇+++++++
class SnippetList(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
  
    """
    name        : SnippetList
    Description : A class that can list all and create a code snippet 
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    
    #method to list all the available code snippets
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    #method to create a code snippet
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
class SnippetDetail(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    """ 
    name        : SnippetDetail
    Description : This class will Retrieve, Update, and Delete a code snippet 
    """
    
    queryset          = Snippet.objects.all()
    serializer_class  = SnippetSerializer
    
    #method to retrieve a code snippet
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    #method to update a code snippet
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    #method to delete a code snippet
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    
    
#        ++++👇👇 Using generic class-based views 👇👇+++++++
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer, UserSerializer
from django.contrib.auth.models import User

from rest_framework import generics

class SnippetListCreate(generics.ListCreateAPIView):
  """
  name        : SnippetListCreate
  description : This class will create a code snippet and list all code snippets
  """
    queryset         = Snippet.objects.all()
    serializer_class = SnippetSerializer
    
    def perform_create(self, serializer):
        serializer.save(ower=self.request.user)
    
class SnippetAllDetail(generics.RetrieveUpdateDestroyAPIView):
  """
  name        : SnippetAllDetail
  description : This class will Reterieve, Update and Delete a code snippets
  """
    queryset         = Snippet.objects.all()
    serializer_class = SnippetSerializer
    
#API for users 
class UserList(generics.ListAPIView):
  """
  name        : UserList
  description : This class will list all Users
  """
    queryset         = User.objects.all()
    serializer_class = UserSerializer
    
class UserDetail(generics.RetrieveAPIView):
  """
  name        : UserList
  description : This class will Retrieve a particular User
  """
    queryset = User.objects.all()
    serializer_class = UserSerializer
