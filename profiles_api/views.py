from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """ test Api View"""

    def get(self,request, format=None):
        """ Returns the List ApiView Feature"""
        an_apiview = [
            'user HTTp method as function(get, post, patch,put,delete)',
            'Is similar to a traditional django View',
            'Gives you the most control over you application logic',
            'Is mappped manually to URls'
        ]

        return Response({'message':'Hello!' ,'an_apiview':an_apiview})