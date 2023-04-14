from rest_framework.response import Response
import rest_framework.status as status
from rest_framework.decorators import api_view
from users.models import Student, Alumni, Company, Credits
from .serializers import StudentSerializer, RegisterSerializer
from django.core import serializers
from jobs.models import Job

@api_view(['POST'])
def login(request):
    if(request.session.get('email')):
        return Response({'message': 'Success'}, status=status.HTTP_200_OK)
    allset=Student.objects.all()
    is_there = allset.filter(email=request.data['email'], password=request.data['password'])
    if(is_there.exists() == False):
        return Response({'message': 'Error! Could not login'}, status=status.HTTP_404_NOT_FOUND)
    # user_json = serializers.serialize('json', is_there)
    request.session['email'] = request.data['email']
    return Response({'message': 'Success'}, status=status.HTTP_200_OK)

@api_view(['POST'])
def register(request):
    batch_object = Credits.objects.all().filter(batch=request.data['batch'], specialization=request.data['specialization'])
    if batch_object.exists() == False:
        return Response({'message': 'Error! Could not register'}, status=status.HTTP_400_BAD_REQUEST)
    batch_object = batch_object[0]
    Student.objects.create(roll_no=request.data['roll_no'], name=request.data['name'], email=request.data['email'], password=request.data['password'], batch=batch_object)
    
    return Response({'message': 'Success'}, status=status.HTTP_200_OK)

@api_view(['POST'])
def logout(request):
    del request.session['email']
    return Response({'message': 'Success'}, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_user(request):
    if(request.session.get('email')):
        email = request.session['email']
        student = Student.objects.all().filter(email=email)
        student_json = serializers.serialize('json', student)
        return Response({'user': student_json}, status=status.HTTP_200_OK)
    return Response({'user': None}, status=status.HTTP_401_UNAUTHORIZED)

@api_view(['GET'])
def get_job(request):
    job=Job.objects.raw("SELECT * FROM Job")
    job_json = serializers.serialize('json', job)
    return Response({'jobs': job_json}, status=status.HTTP_200_OK)


