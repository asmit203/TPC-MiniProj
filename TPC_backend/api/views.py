from rest_framework.response import Response
import rest_framework.status as status
from rest_framework.decorators import api_view
from users.models import Student, Alumni, Company, Credits
from .serializers import StudentSerializer, RegisterSerializer
from django.core import serializers
from jobs.models import Job, Applied
from django.http import FileResponse, Http404
from rest_framework import viewsets,renderers
from django.http import FileResponse
from rest_framework import viewsets, renderers
from rest_framework.decorators import action
from django.http import HttpResponseRedirect
from rest_framework.serializers import ModelSerializer
from rest_framework import exceptions
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .serializers import PostViewSetSerializer


from django.shortcuts import render
import os, json
from django.db import connection

job_counter = 0

@api_view(["GET"])
def view_pdf(request):
    # Replace the filename with the path to your PDF file
    absolute_path = os.path.dirname(__file__)
    # relative_path = os.path.join(absolute_path, "../resume/")
    filename = request.GET['filename']
    # filename = filename[:-1]
    filename = absolute_path + "resume/" + filename
    # print(filename)
    if not os.path.exists(filename):
        raise Http404('File not found')

    
    # Open the file in binary mode
    f = open(filename, "rb")
    response = FileResponse(f, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename=' + os.path.basename(filename)
    return response



@api_view(['POST'])
def login(request):
    if(request.session.get('email')):
        return Response({'message': 'Success'}, status=status.HTTP_200_OK)
    allset=Student.objects.all()
    usertype = str(request.data['user_type'])
    if(usertype == 'alumni'):
        is_there = Alumni.objects.all().filter(email=request.data['email'], password=request.data['password'])
        if(is_there.exists() == False):
            return Response({'message': 'Error! Could not login Alumni'}, status=status.HTTP_404_NOT_FOUND)
        # user_json = serializers.serialize('json', is_there)
        request.session['email'] = request.data['email']
        request.session['user_type'] = request.data['user_type']
        return Response({'message': 'Success'}, status=status.HTTP_200_OK)
    
    elif(usertype == 'student'):
        is_there = Student.objects.all().filter(email=request.data['email'], password=request.data['password'])
        if(is_there.exists() == False):
            return Response({'message': 'Error! Could not login Student'}, status=status.HTTP_404_NOT_FOUND)
        # user_json = serializers.serialize('json', is_there)
        request.session['email'] = request.data['email']
        request.session['user_type'] = request.data['user_type']
        return Response({'message': 'Success'}, status=status.HTTP_200_OK)
    
    elif(usertype == 'company'):
        is_there = Company.objects.all().filter(email=request.data['email'], password=request.data['password'])
        if(is_there.exists() == False):
            return Response({'message': 'Error! Could not login'}, status=status.HTTP_404_NOT_FOUND)
        # user_json = serializers.serialize('json', is_there)
        request.session['email'] = request.data['email']
        request.session['user_type'] = request.data['user_type']
        return Response({'message': 'Success'}, status=status.HTTP_200_OK)

@api_view(['POST'])
def register(request):
    # batch_object = Credits.objects.all().filter(
    #     batch=request.data['batch'], 
    #     specialization=request.data['specialization'])
    usertype = request.data['user_type']
    if(usertype == 'alumni'):
        # batch = request.data['batch'] 
        Alumni.objects.create(
            roll_no=request.data['roll_no'], 
            name=request.data['name'], 
            email=request.data['email'], 
            password=request.data['password']
        )
        return Response({'message': 'Success'}, status=status.HTTP_200_OK)

    elif(usertype == 'company'):
        cid = request.data['name'] + "_"
        cid += request.data['email']
        cid = cid.replace("@", "_")
        cid = cid.replace(".", "_")
        Company.objects.create(cid=cid, name=request.data['name'], email=request.data['email'], password=request.data['password'])
        return Response({'message': 'Success'}, status=status.HTTP_200_OK)

    elif(usertype == 'student'):
        # if batch_object.exists() == False:
        #     return Response({'message': 'Error! Could not register'}, status=status.HTTP_400_BAD_REQUEST)
        # batch_object = batch_object[0]
        Student.objects.create(
            roll_no=request.data['roll_no'], 
            name=request.data['name'], 
            email=request.data['email'], 
            password=request.data['password']
            )
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
    job=Job.objects.raw("SELECT * FROM jobs_job")
    job_json = serializers.serialize('json', job)
    return Response({'jobs': job_json}, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_applied(request):
    eml = request.session['email']
    rn = Student.objects.all().filter(email=eml)
    # jobappl = Applied.objects.all().filter(roll_no = rn)

    rn = rn.first().roll_no
    # print()
    applied=Applied.objects.all().filter(roll_no=rn)
    # jobappl = JobApplied.objects.all().filter(jid=applied.
    jobarr = []
    # company_list = []
    # print(type(applied[0].jid))
    for jids in applied.values():
        # print(jids)
        jj =  jids["jid_id"]
        ll = Job.objects.all().filter(jid =jj)
        # compname = Company.objects.filter(cid = ll.first().cid)
        # company_list.append([compname.first().name, str(ll.first().jid.title),ll.first().jobTitle,ll.first().jobDesc,ll.first().flag_job,ll.first().cid,ll.first().minQual,ll.first().ctc])
        new = ll.first()
        # print(type(new))
        # new.name = compname.first().name
        jobarr.append(ll.first())
        # jobarr.append(new)
    # print(company_list)
    # applied_json = json.dumps(company_list, indent = 4) 
    applied_json = serializers.serialize('json', jobarr)
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
        rn = rn.first().roll_no
        jid = request.data['jid']
        # Applied.objects.create(roll_no=rn, jid=jid,status=True)
        with connection.cursor() as cursor:
            cursor.execute("INSERT INTO jobs_applied(jid_id,status,roll_no_id) VALUES(%s,%s,%s)" ,[jid,"queue",rn])

        return Response({'message': 'Success'}, status=status.HTTP_200_OK)
    return Response({'message': 'Error! Could not apply'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def add_job(request):
    if(request.session.get('email')):
        eml = request.session['email']
        cid = Company.objects.all().filter(email=eml)
        cid = cid.values("cid").first()["cid"]
        jid = cid.replace('_', '')
        global job_counter 
        job_counter+=1
        # Job.objects.create(cid=cid, jid=request.data['jid'], title=request.data['title'], description=request.data['description'])
        with connection.cursor() as cursor:
            cursor.execute("INSERT INTO jobs_job(cid_id,jid,jobTitle,jobDesc,flag_job,minQual,ctc) VALUES(%s,%s,%s,%s,%s,%s,%s)" ,[cid,job_counter,request.data['jobTitle'],request.data['jobDesc'],request.data['flag_job'],request.data['minQual'],request.data['ctc']])
        return Response({'message': 'Success'}, status=status.HTTP_200_OK)
    return Response({'message': 'Error! Could not add job'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def update_profile(request):
    if(request.session.get('email')):
        usertype = request.session['user_type']
        email = request.session['email']
        if(usertype == 'student'):
            with connection.cursor() as cursor:
                    cursor.execute("UPDATE users_student SET batch_id = %s WHERE email = %s" ,[str(request.data["batch"]),request.data['email']])
            stud = Student.objects.get(email=email)
            stud.name=request.data['name']
            stud.email=request.data['email']
            stud.password=request.data['password']
            stud.roll_no=request.data['roll_no']
            stud.cgpa=request.data['CGPA']
            stud.areaofInterest=request.data['areaofinterest']
            stud.m10=request.data['m10']
            stud.m11=request.data['m11']
            stud.m12=request.data['m12']
            stud.msem1=request.data['msem1']
            stud.msem2=request.data['msem2']
            stud.msem3=request.data['msem3']
            stud.msem4=request.data['msem4']
            stud.msem5=request.data['msem5']
            stud.msem6=request.data['msem6']
            stud.msem7=request.data['msem7']
            stud.msem8=request.data['msem8']
            stud.studprofilepic=request.data['studprofilepic']
            stud.save()

            return Response({'message': 'Success'}, status=status.HTTP_200_OK)
        elif(usertype == 'alumni'):
            with connection.cursor() as cursor:
                cursor.execute("UPDATE users_alumni SET batch_id = %s WHERE email = %s" ,[request.data["batch"],request.data['email']])
                cursor.execute("UPDATE users_alumni SET cid_id = %s WHERE email = %s;", [request.data["cid"], request.data['email']])
            alum = Alumni.objects.get(email=email)
            alum.name=request.data['name']
            alum.email=request.data['email']
            alum.password=request.data['password']
            print(request.data['roll_no'])
            alum.roll_no=request.data['roll_no']
            alum.cgpa=request.data['CGPA']
            alum.company=request.data['company']
            alum.designation=request.data['designation']
            alum.m10=request.data['m10']
            alum.m11=request.data['m11']
            alum.m12=request.data['m12']
            alum.msem1=request.data['msem1']
            alum.msem2=request.data['msem2']
            alum.msem3=request.data['msem3']
            alum.msem4=request.data['msem4']
            alum.msem5=request.data['msem5']
            alum.msem6=request.data['msem6']
            alum.msem7=request.data['msem7']
            alum.msem8=request.data['msem8']
            alum.alumprofilepic=request.data['alumprofilepic']
            alum.save()
            return Response({'message': 'Success alumni'}, status=status.HTTP_200_OK)
        elif(usertype == 'company'):
            comp = Company.objects.get(email=email)
            comp.name=request.data['name'] 
            comp.email=request.data['email'] 
            comp.password=request.data['password']
            comp.reqCandDet=request.data['reqCandDet']
            comp.marksCriteria=request.data['marksCriteria']
            comp.salaryPackage=request.data['salaryPackage']
            comp.mode_of_interview=request.data['mode_of_interview']
            comp.time_of_start_iitp=request.data['time_of_start_iitp']
            comp.companypic=request.data['companypic']
            comp.save()
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
  

#company see what they have posted
@api_view(["GET"])
def job_posted(request):
    eml = request.session['email']
    cid = Company.objects.all().filter(email=eml)
    # jobappl = Applied.objects.all().filter(roll_no = rn)

    # cid = cid[0].cid
    cid = cid.first().cid
    # print()
    applied=Job.objects.all().filter(cid=cid)
    # jobappl = JobApplied.objects.all().filter(jid=applied.
    jobarr = []
    # print(type(applied[0].jid))
    for jids in applied.values():
        # print(jids)
        jj =  jids["jid"]
        ll = Job.objects.all().filter(jid =jj)
        jobarr.append(ll.first())
    applied_json = serializers.serialize('json', jobarr)
    return Response({'applied': applied_json}, status=status.HTTP_200_OK)

#company see who applied 
@api_view(["GET"])
def whoapplied(request):
    eml = request.session['email']
    cid = Company.objects.all().filter(email=eml)
    # jobappl = Applied.objects.all().filter(roll_no = rn)

    cid = cid[0].cid
    # print()
    jobappl = Job.objects.all().filter(cid=cid)
    jobarr = []
    # print(type(applied[0].jid))
    for jb in jobappl.values():
        applied=Applied.objects.all().filter(jid=jb['jid'])
        for jids in applied.values():
            print(jids)
            jj =  jids["roll_no_id"]
            ll = Student.objects.all().filter(roll_no =jj)
            jobarr.append(ll.first())
    applied_json = serializers.serialize('json', jobarr)
    return Response({'applied': applied_json}, status=status.HTTP_200_OK)

#resume upload and modification
@api_view(["POST"])
def upload_resume(request):
    eml = request.session['email']
    stud = Student.objects.all().filter(email=eml)
    stud.resume = request.data.get('resume')
    # serializer_class = PostViewSetSerializer
    # # permission_classes = (IsAuthenticated,)
    # # http_method_names = ['post', ]

    # def create(self, request, *args, **kwargs):
    #     data = {
    #         "title": request.data.get('title'),
    #         "resume": request.FILES.get(),
    #         }
    #     _serializer = self.serializer_class(data=data)
    #     if _serializer.is_valid():
    #         _serializer.save()
    #         return Response(data=_serializer.data, status=status.HTTP_201_CREATED)  # NOQA
    #     else:
    #         return Response(data=_serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # NOQA
    # if request.session['user_type'] == 'student':
    #     eml = request.session['email']
    #     if request.method == "POST":
    #         # instance = Student.objects.all().filter(email=eml).update(resume=request.FILES["resume"])
    #         # instance.save()
    #         # print(request.FILES)
    #         # print("jijqeifhewoifh")
    #         # print(request.data)
    #         # print("hiii")
            
    #         # print("hemlo")
    #         Student.objects.all().filter(email=eml).update(resume=request.FILES)
    #         return Response({'message': 'Success'}, status=status.HTTP_200_OK)
    #     else:
    #         return Response({'message': 'Error! Could not update profile'}, status=status.HTTP_400_BAD_REQUEST)
    # else:
    #     return Response({'message': 'Error! Permission Denied !!'}, status=status.HTTP_400_BAD_REQUEST)


    
#job status by company
@api_view(["POST"])
def job_status(request):
    if request.session['user_type'] == 'student':
        eml = request.session['email']
        if request.method == "POST":
            cid= Company.objects.all().filter(email=eml).first().cid
            jid = request.data['jid']
            roll_no = request.data['roll_no']
            status = request.data['status']
            Applied.objects.all().filter(jid=jid,roll_no=roll_no).update(status=status)
            return Response({'message': 'Success'}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Error! Could not update profile'}, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({'message': 'Error! Permission Denied !!'}, status=status.HTTP_400_BAD_REQUEST)
    
#list of batches
@api_view(["GET"])
def batch_list(request):
    batch = Credits.objects.all()
    listbatch = []
    for i in batch.values():
        listbatch.append(i["batch"])
    print(listbatch)
    batch_json = json.dumps(listbatch, indent = 4) 
    return Response({'batch': batch_json}, status=status.HTTP_200_OK)

#list of batches
@api_view(["GET"])
def company_list(request):
    batch = Company.objects.all()
    listbatch = []
    for i in batch.values():
        listbatch.append(i["name"])
    print(listbatch)
    batch_json = json.dumps(listbatch, indent = 4) 
    return Response({'cid': batch_json}, status=status.HTTP_200_OK)

@api_view(["GET"])
def cpi_cal(request):
    eml = request.session['email']
    user = request.session['user_type']
    if user == 'student':
        stud = Student.objects.all().filter(email=eml)
        stud = stud.first()
        batch = stud.batch
        credits = Credits.objects.all().filter(batch=batch)
        cred = credits.first().credits5
        print(cred)
        cpi = 0
        sumCred = int(credits.first().credits1) + int(credits.first().credits2) + int(credits.first().credits3) +int(credits.first().credits4) + int(credits.first().credits5) +int(credits.first().credits6) +int(credits.first().credits7) +int(credits.first().credits8) 
        cpi = int(credits.first().credits1)*int(stud.msem1) + int(credits.first().credits2)*int(stud.msem2) + int(credits.first().credits3)*int(stud.msem3) +int(credits.first().credits4)*int(stud.msem4) + int(credits.first().credits5)*int(stud.msem5) +int(credits.first().credits6)*int(stud.msem6) +int(credits.first().credits7)*int(stud.msem7) +int(credits.first().credits8)*int(stud.msem8) 
        cpi = cpi/sumCred
        return Response({'cpi': str(cpi)}, status=status.HTTP_200_OK)