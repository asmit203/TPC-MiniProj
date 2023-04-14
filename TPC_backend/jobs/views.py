from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Job
from .models import Applied
from django.contrib.auth.decorators import login_required
from users.models import Company, Student, Credits, Alumni

# def job_search(request):
#     jobs = job.objects.all()
#     credits = Credits.objects.all()
#     # company = Company.objects.all()
#     # company_id = request.users.company.cid
#     # company = Company.objects.get(cid=company_id)
#     # min_qual = company.minQual
#     if 'search' in request.GET:
#         search_term = request.GET['search']
#         jobs = jobs.filter(jobTitle__icontains=search_term)

#     # if 'minQual' in request.GET:
#     #     minQual = request.GET['minQual']
#     #     jobs = jobs.filter(minQual__icontains=minQual)

#     if 'ctc' in request.GET:
#         ctc = request.GET['ctc']
#         jobs = jobs.filter(ctc__icontains=ctc)

#     context = {
#         'jobs': jobs
#     }
#     return render(request, 'job_search.html', context)
