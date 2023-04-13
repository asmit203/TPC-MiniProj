from rest_framework.response import Response
import rest_framework.status as status
from rest_framework.decorators import api_view
from users.models import Student, Alumni, Company, Credits
from .serializers import LoginSerializer, RegisterSerializer


@api_view(['POST'])
def login(request):
    allset=Student.objects.all()
    is_there = allset.filter(email=request.data['email'], password=request.data['password'])
    if(is_there.exists() == False):
        return Response({'message': 'Error! Could not login'}, status=status.HTTP_404_NOT_FOUND)
    return Response({'message': 'Success'}, status=status.HTTP_200_OK)

@api_view(['POST'])
def register(request):
    batch_object = Credits.objects.all().filter(batch=request.data['batch'], specialization=request.data['specialization'])
    if batch_object.exists() == False:
        return Response({'message': 'Error! Could not register'}, status=status.HTTP_400_BAD_REQUEST)
    batch_object = batch_object[0]
    student = Student.objects.create(roll_no=request.data['roll_no'], name=request.data['name'], email=request.data['email'], password=request.data['password'], batch=batch_object)
    
    return Response({'message': 'Success'}, status=status.HTTP_200_OK)