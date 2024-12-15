from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets

from profiles_api import serializers

class HelloApiView(APIView):
    """Test API view"""
    serializer_class = serializers.HelloSerializer

    def get(self, request, form=None):
        """Returns a list of API views features"""
        an_apiview = ['Uses HTTP methods as function (get, post, patch, put, delete)',
        'Is similar to a traditional Django View',
        'Gives you the most control over the application logic',
        'Is mapped manually to URLs']

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})
    

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

    def put(self, request, pk=None):
        """Handle updating the object"""
        return Response({'method': 'PUT'})
    

    def patch(self, request, pk=None):
        """Handle partial update"""
        return Response({'method': 'PATCH'})
    

    def delete(self, request, pk=None):
        """Delete an object"""
        return Response({'method': 'DELETE'})
    


class HelloViewSet(viewsets.ViewSet):
    """Test Api viewSet"""

    serializer_class = serializers.HelloSerializer


    def list(self, request):
        """Return a hello message"""
        a_viewset = ['Uses actions (list, create, retrieve, update, partial_update)'
                     'Automatically maps to URLs using routers',
                     'Provide more functionalit with less code',]

        return Response({'message': 'Hello!', 'a_viewset': a_viewset})
    

    def create(self, request):
        """Create a new hello message"""
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}!'
            return Response({'message': message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

    def retrieve(self, requeat, pk=None):
        """Handle getting object by its ID"""
        return Response({'http_method': 'GET'})
    
    
    def update(self, request, pk=None):
        """handle updateing the object"""
        return Response({'http_method': 'PUT'})
    

    def partial_update(self, request, pk=None):
        """Handle partial update"""
        return Response({'http_method': 'PATCH'})
    
    def destroy(self, request, pk=None):
        """Handle removing an object"""
        return Response({'http_method': 'DELETE'})

