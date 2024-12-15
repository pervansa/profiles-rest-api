from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
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