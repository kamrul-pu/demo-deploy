from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class Home(APIView):
    def get(self, request, format=None):
        return Response(
            {"name": "Demo App", "version": 1.0, "release": "Initial Release"},
            status=status.HTTP_200_OK,
        )
