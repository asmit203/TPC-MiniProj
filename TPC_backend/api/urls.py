from django.urls import path, re_path
from . import views

urlpatterns = [
    path('login/', views.login),
    path('register/', views.register),
    path('user/', views.get_user),
    path('logout/', views.logout),
    path('profile/', views.get_profile),
    path('applied/', views.get_applied),
    path('whoapplied/', views.whoapplied),
    path('getjobs/', views.get_job),
    path('apply/', views.apply),
    path('addjob/', views.add_job),
    path('updateprofile/', views.update_profile),
    path('deletejob/', views.delete_job),
    path('deleteprofile/', views.delete_profile),
    path('jobpostedbycompany/', views.job_posted),
    path('whoappliedcompany/', views.whoapplied),
    path('uploadresume/', views.upload_resume),
    path('batchlist/', views.batch_list),
    path('cidlist/', views.company_list),   
    path('getcpi/', views.cpi_cal),   
    re_path(r'^viewpdf/$', views.view_pdf),
]
