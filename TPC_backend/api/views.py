from rest_framework.response import Response
import rest_framework.status as status
from rest_framework.decorators import api_view
from users.models import Student, Alumni, Company
from .serializers import LoginSerializer, RegisterSerializer


@api_view(['POST'])
def login(request):
    serializer = LoginSerializer(data=request.data)
    if not serializer.is_valid():
        return Response({'message': 'Error! Could not login'}, status=status.HTTP_400_BAD_REQUEST)
    return Response({'message': 'Success'}, status=status.HTTP_200_OK)

@api_view(['POST'])
def register(request):
    serializer = RegisterSerializer(data=request.data)
    if not serializer.is_valid():
        return Response({'message': 'Error! Could not register'}, status=status.HTTP_400_BAD_REQUEST)
    serializer.save()
    return Response({'message': 'Success'}, status=status.HTTPS_200_OK)