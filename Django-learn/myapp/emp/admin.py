from django.contrib import admin
from emp.models import Emp, Feedback

# Register your models here.
class EmpAdmin(admin.ModelAdmin) : 
    list_display = ('emp_id', 'name', 'department', 'working')
    list_editable = ('name','department')
    search_fields = ('emp_id',)
    

admin.site.register(Emp, EmpAdmin)
admin.site.register(Feedback)