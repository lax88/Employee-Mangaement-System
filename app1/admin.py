from django.contrib import admin
from .models import Employee
from .models import Project
from .models import Attendance

# Register your models here.
@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display=['id','name','email','mobile','date_of_birth','gender','skills','state','profile_picture','resume','video']

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display=['id','title','description','start_date','end_date','employees_assigned_list']

    def employees_assigned_list(self, obj):
        return ",".join([employee.name for employee in obj.employees_assigned.all()])
    employees_assigned_list.short_description = "Employees Assigned"

@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display=['id','date','employee','status']
    