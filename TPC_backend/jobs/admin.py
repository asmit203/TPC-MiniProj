from django.contrib import admin

# Register your models here.
from django.contrib import admin
from jobs.models import job,applied
# Register your models here..

class jobAdmin(admin.ModelAdmin):
    pass
      
    
class appliedAdmin(admin.ModelAdmin):
    pass
    

admin.site.register(job,jobAdmin)
admin.site.register(applied,appliedAdmin)