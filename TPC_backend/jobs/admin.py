from django.contrib import admin

# Register your models here.
from django.contrib import admin
from jobs.models import job,applied
# Register your models here..

class jobAdmin(admin.ModelAdmin):
    list_display = ['cid','jid','jobTitle','jobDesc']    
    
class appliedAdmin(admin.ModelAdmin):
    list_display = ['jid','roll_no','status','sid']

admin.site.register(job,jobAdmin)
admin.site.register(applied,appliedAdmin)