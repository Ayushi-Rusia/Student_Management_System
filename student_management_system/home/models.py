from django.db import models

# Create your models here.
class User(models.Model):
    Name=models.CharField(max_length=20)
    Email=models.CharField(max_length=20)
    Password=models.CharField(max_length=20,blank=True,null=True)
    is_active=models.BooleanField(default=True)
    def __str__(self):
        return self.Name

class Course(models.Model):
    Name=models.CharField(max_length=20)
    Fees=models.IntegerField()
    Duration=models.CharField(max_length=20)
    TextField=models.CharField(max_length=20)
    is_active=models.BooleanField(default=True)
    def __str__(self):
        return self.Name
class Student(models.Model):
    Name=models.CharField(max_length=20)
    Email=models.CharField(max_length=20)
    Contact=models.IntegerField()
    College=models.CharField(max_length=20)
    Degree=models.CharField(max_length=20)
    course=models.ForeignKey(Course,on_delete=models.CASCADE)
    Total=models.IntegerField(default=0)
    Paid=models.IntegerField(default=0)
    Due=models.IntegerField(default=0)
    is_active=models.BooleanField(default=True)
    def __str__(self):
        return self.Name
    
class Teacher(models.Model):
    Emp_Id = models.CharField(max_length=100)
    Name = models.CharField(max_length=100)
    Email = models.EmailField(max_length=100)
    Mobile = models.CharField(max_length=10)
    Joining_Date = models.CharField(max_length=255)
    Education = models.CharField(max_length=100)
    Expriance = models.CharField(max_length=100)
    Privies_salary = models.FloatField()  
    is_active=models.BooleanField(default=True)
    def __str__(self):
        return self.Name

    
