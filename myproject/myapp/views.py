from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class AddNumbersView(APIView):
    def post(self, request, *args, **kwargs):
        num1 = float(request.data.get('num1'))
        num2 = float(request.data.get('num2'))
        result = num1 + num2
        return Response({"result": result}, status=status.HTTP_200_OK)
