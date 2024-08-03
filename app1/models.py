from django.db import models

# Create your models here.
class Employee(models.Model):
    GENDER_CHOICES=[("Male","male"),("Female","female"),("others","others")]
    STATE_CHOICES=[("1","Koshi"),("2","Madhesh"),("3","Bagmati"),("4","Gandaki"),("5","Lumbini"),("6","Karnali"),("7","Sudhurpaschim")]

    name=models.CharField(max_length=255)
    email=models.EmailField()
    mobile=models.PositiveIntegerField()
    date_of_birth=models.DateField(auto_now_add=False, auto_now=False,null=True)
    gender=models.CharField(max_length=25, choices=GENDER_CHOICES, default='others')
    skills=models.CharField(max_length=100,null=True,blank=True)
    state=models.CharField(max_length=25, choices=STATE_CHOICES, default="3")
    profile_picture=models.ImageField(upload_to="employee_profile_picture/",null=True,blank=True)
    resume=models.FileField(upload_to="employee_resume/",null=True,blank=True)
    video=models.FileField(upload_to="employee_video/",null=True,blank=True)


    def __str__(self):
        return self.name
    
class Project(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.DateField(auto_now=False, auto_now_add=False)
    end_date = models.DateField(auto_now=False, auto_now_add=False)
    employees_assigned = models.ManyToManyField(Employee)

    def __str__(self):
        return self.title

class Attendance(models.Model):
    STATUS_CHOICES = [
        ('present', 'Present'),
        ('absent', 'Absent'),
        ('late', 'Late'),
    ]

    date = models.DateField(auto_now=False, auto_now_add=False)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)

    def __str__(self):
        return f'{self.employee.name} on {self.date} ({self.status})'