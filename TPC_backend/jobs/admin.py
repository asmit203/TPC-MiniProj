from django.contrib import admin

# Register your models here.
from django.contrib import admin
from jobs.models import job,applied
# Register your models here..

class jobAdmin(admin.ModelAdmin):
    list_display = [field.name for field in job._meta.get_fields()]

    
    
class appliedAdmin(admin.ModelAdmin):
    list_display = [field.name for field in applied._meta.get_fields()]

admin.site.register(job,jobAdmin)
admin.site.register(applied,appliedAdmin)