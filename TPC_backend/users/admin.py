from django.contrib import admin
from users.models import Student, Company, Alumni, Credits
# Register your models here.

admin.site.register(Company)
admin.site.register(Student)
admin.site.register(Alumni)
admin.site.register(Credits)
