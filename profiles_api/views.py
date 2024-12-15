from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test API view"""
    def get(self, request, form=None):
        """Returns a list of API views features"""
        an_apiview = ['Uses HTTP methods as function (get, post, patch, put, delete)',
        'Is similar to a traditional Django View',
        'Gives you the most control over the application logic',
        'Is mapped manually to URLs']

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})
