from rest_framework.response import Response
import rest_framework.status as status
from rest_framework.decorators import api_view
from users.models import Student, Alumni, Company
from .serializers import StudentSerializer


@api_view(['POST'])
def login(request):
    serializer = StudentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    else:
        return Response({'message': 'Error! Could not login'}, status=status.HTTP_400_BAD_REQUEST)
    return Response(serializer.data)
