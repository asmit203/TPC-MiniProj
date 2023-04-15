from rest_framework.response import Response
import rest_framework.status as status
from rest_framework.decorators import api_view
from users.models import Student, Alumni, Company, Credits
from .serializers import StudentSerializer, RegisterSerializer
from django.core import serializers
from jobs.models import Job, Applied

@api_view(['POST'])
def login(request):
    if(request.session.get('email')):
        return Response({'message': 'Success'}, status=status.HTTP_200_OK)
    allset=Student.objects.all()
    usertype = request.data['user_type']
    if(usertype == 'alumni'):
        is_there = allset.filter(email=request.data['email'], password=request.data['password'])
        if(is_there.exists() == False):
            return Response({'message': 'Error! Could not login'}, status=status.HTTP_404_NOT_FOUND)
        # user_json = serializers.serialize('json', is_there)
        request.session['email'] = request.data['email']
        request.session['user_type'] = request.data['user_type']
        return Response({'message': 'Success'}, status=status.HTTP_200_OK)
    
    elif(usertype == 'student'):
        is_there = allset.filter(email=request.data['email'], password=request.data['password'])
        if(is_there.exists() == False):
            return Response({'message': 'Error! Could not login'}, status=status.HTTP_404_NOT_FOUND)
        # user_json = serializers.serialize('json', is_there)
        request.session['email'] = request.data['email']
        request.session['user_type'] = request.data['user_type']
        return Response({'message': 'Success'}, status=status.HTTP_200_OK)
    
    elif(usertype == 'company'):
        is_there = allset.filter(email=request.data['email'], password=request.data['password'])
        if(is_there.exists() == False):
            return Response({'message': 'Error! Could not login'}, status=status.HTTP_404_NOT_FOUND)
        # user_json = serializers.serialize('json', is_there)
        request.session['email'] = request.data['email']
        request.session['user_type'] = request.data['user_type']
        return Response({'message': 'Success'}, status=status.HTTP_200_OK)

@api_view(['POST'])
def register(request):
    batch_object = Credits.objects.all().filter(batch=request.data['batch'], specialization=request.data['specialization'])
    usertype = request.data['user_type']
    if(usertype == 'alumni'):
        Alumni.objects.create(roll_no=request.data['roll_no'], name=request.data['name'], email=request.data['email'], password=request.data['password'])
        return Response({'message': 'Success'}, status=status.HTTP_200_OK)

    elif(usertype == 'company'):
        cid = request.data['name'] + "_"
        cid += request.data['email']
        Company.objects.create(cid=cid, name=request.data['name'], email=request.data['email'], password=request.data['password'])
        return Response({'message': 'Success'}, status=status.HTTP_200_OK)

    elif(usertype == 'student'):
        if batch_object.exists() == False:
            return Response({'message': 'Error! Could not register'}, status=status.HTTP_400_BAD_REQUEST)
        batch_object = batch_object[0]
        Student.objects.create(roll_no=request.data['roll_no'], name=request.data['name'], email=request.data['email'], password=request.data['password'], batch=batch_object)
        return Response({'message': 'Success'}, status=status.HTTP_200_OK)
    else:
        return Response({'message': 'Error! Could not register'}, status=status.HTTP_400_BAD_REQUEST)
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

@api_view(['GET'])
def get_applied(request):
    eml = request.session['email']
    rn = Student.objects.all().filter(email=eml)

    rn = rn[0].roll_no

    applied=Applied.objects.all().filter(roll_no=rn)
    applied_json = serializers.serialize('json', applied)
    return Response({'applied': applied_json}, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_profile(request):
    if(request.session.get('email')):
        usertype = request.session['user_type']
        email = request.session['email']
        if(usertype == 'student'):
            student = Student.objects.all().filter(email=email)
            student_json = serializers.serialize('json', student)
            return Response({'profile': student_json,'user_type':usertype}, status=status.HTTP_200_OK)
        elif(usertype == 'alumni'):
            alumni = Alumni.objects.all().filter(email=email)
            alumni_json = serializers.serialize('json', alumni)
            return Response({'profile': alumni_json,'user_type':usertype}, status=status.HTTP_200_OK)
        elif(usertype == 'company'):
            company = Company.objects.all().filter(email=email)
            company_json = serializers.serialize('json', company)
            return Response({'profile': company_json,'user_type':usertype}, status=status.HTTP_200_OK)
    return Response({'profile': None}, status=status.HTTP_401_UNAUTHORIZED)


@api_view(['POST'])
def apply(request):
    if(request.session.get('email')):
        eml = request.session['email']
        rn = Student.objects.all().filter(email=eml)
        rn = rn[0]['roll_no']
        jid = request.data['jid']
        Applied.objects.create(roll_no=rn, jid=jid,status=True)
        return Response({'message': 'Success'}, status=status.HTTP_200_OK)
    return Response({'message': 'Error! Could not apply'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def add_job(request):
    if(request.session.get('email')):
        eml = request.session['email']
        cid = Company.objects.all().filter(email=eml)
        cid = cid[0]['cid']
        Job.objects.create(cid=cid, jid=request.data['jid'], title=request.data['title'], description=request.data['description'])
        return Response({'message': 'Success'}, status=status.HTTP_200_OK)
    return Response({'message': 'Error! Could not add job'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def update_profile(request):
    if(request.session.get('email')):
        usertype = request.session['user_type']
        email = request.session['email']
        if(usertype == 'student'):
            Student.objects.filter(email=email).update(name=request.data['name'], email=request.data['email'], password=request.data['password'])
            return Response({'message': 'Success'}, status=status.HTTP_200_OK)
        elif(usertype == 'alumni'):
            Alumni.objects.filter(email=email).update(name=request.data['name'], email=request.data['email'], password=request.data['password'])
            return Response({'message': 'Success'}, status=status.HTTP_200_OK)
        elif(usertype == 'company'):
            Company.objects.filter(email=email).update(name=request.data['name'], email=request.data['email'], password=request.data['password'])
            return Response({'message': 'Success'}, status=status.HTTP_200_OK)
    return Response({'message': 'Error! Could not update profile'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def delete_job(request):
    if(request.session.get('email')):
        eml = request.session['email']
        cid = Company.objects.all().filter(email=eml)
        cid = cid[0]['cid']
        jid = request.data['jid']
        Job.objects.filter(cid=cid, jid=jid).delete()
        return Response({'message': 'Success'}, status=status.HTTP_200_OK)
    return Response({'message': 'Error! Could not delete job'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def delete_profile(request):
    if(request.session.get('email')):
        usertype = request.session['user_type']
        email = request.session['email']
        if(usertype == 'student'):
            Student.objects.filter(email=email).delete()
            return Response({'message': 'Success'}, status=status.HTTP_200_OK)
        elif(usertype == 'alumni'):
            Alumni.objects.filter(email=email).delete()
            return Response({'message': 'Success'}, status=status.HTTP_200_OK)
        elif(usertype == 'company'):
            Company.objects.filter(email=email).delete()
            return Response({'message': 'Success'}, status=status.HTTP_200_OK)
    return Response({'message': 'Error! Could not delete profile'}, status=status.HTTP_400_BAD_REQUEST)
  

@api_view(['POST'])
def logout_cop(request):
    try:
        del request.session['email']
        del request.session['user_type']
    except KeyError:
        pass
    return Response({'message': 'Success'}, status=status.HTTP_200_OK)

#get resume
# @api_view(['GET'])
# def get_resume(request):
#     if(request.session.get('email')):
#         usertype = request.session['user_type']
#         email = request.session['email']
#         if(usertype == 'student'):
#             student = Student.objects.all().filter(email=email)
#             student_json = serializers.serialize('json', student)
#             return Response({'resume': student_json,'user_type':usertype}, status=status.HTTP_200_OK)
#         elif(usertype == 'alumni'):
#             alumni = Alumni.objects.all().filter(email=email)
#             alumni_json = serializers.serialize('json', alumni)
#             return Response({'resume': alumni_json,'user_type':usertype}, status=status.HTTP_200_OK)
#     return Response({'resume': None}, status=status.HTTP_401_UNAUTHORIZED)