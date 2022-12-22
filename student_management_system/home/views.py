from django.shortcuts import render,redirect
from . models import *
from django.contrib.auth.hashers import check_password, make_password
from django.contrib import messages
from django.contrib import auth

# Create your views here.
def index(request):
    return render(request,'index.html')

def login(request):
    if request.method=="POST":
        Name=request.POST['name']
        Password=request.POST['password']
        if User.objects.filter(Name=Name).exists():
            user = User.objects.get(Name=Name)
            password=user.Password
            if check_password(Password,password):
                messages.success(request,"Login Successful")
                return render(request,'dashboard.html')
            else:
                messages.info(request,'Password Incorrect')
                return render(request,'index.html')
        else:
            messages.info(request,'User Name Incorrect')
            return render(request,'index.html')
    else:
        return render(request,'index.html')

def signup(request):
     return render(request,'signup.html')

def formdata(request):
    if request.method== 'POST':
        Name=request.POST['name']
        Email=request.POST['email']
        Password=make_password(request.POST['password'])
        if User.objects.filter(Email=Email).exists():
            messages.error(request, "This email is already exist")
            return render(request,'signup.html')
        else:
            user=User.objects.create(Name=Name,Email=Email,Password=Password)
            user.save()
            return render(request,'index.html')

def dashboard(request):
    data=Course.objects.all()
    x=Course.objects.all().count()
    y=Student.objects.all().count()
    z=Teacher.objects.all().count()
    return render(request,'dashboard.html',{'data':data,'x':x,'y':y,'z':z})

def course (request):
    data=Course.objects.all()
    return render(request,'course.html',{'data':data})

def add_course(request):
    Name=request.POST['name']
    Fees=request.POST['fees']
    Fees=int(Fees)
    Duration=request.POST['duration']
    TextField=request.POST['area']
    if Course.objects.filter(Name=Name).exists():
        messages.info(request,'Course already exists')
        return render(request,"course.html")
    else:
        Course.objects.create(Name=Name,
                                Fees=Fees,
                                TextField=TextField,
                                Duration=Duration)
        messages.success(request,'!!!!Successfully Added!!!!')
        data=Course.objects.all()
        return render(request,'course.html',{'data':data})

def update_course(request):
    c=Course()
    c.id=request.POST['uid']
    c.Name=request.POST['name']
    c.Fees=request.POST['fees']
    c.Fees=int(c.Fees)
    c.Duration=request.POST['duration']
    c.TextField=request.POST['area']
    c.save()
    data=Course.objects.all()
    s_data=Student.objects.all()
    return render(request,'course.html',{'data':data,'s_data':s_data})

def delete_course(request):
    cid=request.GET['cid']
    Course.objects.get(id=cid).delete()
    data=Course.objects.all()
    s_data=Student.objects.all()
    return render(request,'course.html',{'s_data':s_data,'data':data})

def student (request):
    s_data=Student.objects.all()
    data=Course.objects.all()
    return render(request,'viewstudents.html',{'s_data':s_data,"data":data})

def add_student(request):
    s=Student()
    s.Name=request.POST['name']
    s.Email=request.POST['email']
    s.Contact=request.POST['contact']
    s.College=request.POST['college']
    s.Degree=request.POST['degree']
    s.Total=request.POST['total']
    # s.Paid=request.POST['paid']
    # s.Due=request.POST['due']
    s.course=Course.objects.get(id=(request.POST['course']))
    s.save()
    data=Course.objects.all()
    s_data=Student.objects.all()
    return render(request,'viewstudents.html',{'s_data':s_data,'data':data})

def update_student(request):
    s=Student()
    s.id=request.POST['uid']
    s.Name=request.POST['name']
    s.Email=request.POST['email']
    s.Contact=request.POST['contact']
    s.College=request.POST['college']
    s.Degree=request.POST['degree']
    s.Total=request.POST['total']
    s.Paid=request.POST['paid']
    s.Due=request.POST['due']
    cid=request.POST['course']
    s.course=Course.objects.get(id=cid)
    s.save()
    data=Course.objects.all()
    s_data=Student.objects.all()
    return render(request,'viewstudents.html',{'data':data,'s_data':s_data})

def delete_student(request):
    sid=request.GET['sid']
    Student.objects.get(id=sid).delete()
    data=Course.objects.all()
    s_data=Student.objects.all()
    return render(request,'viewstudents.html',{'s_data':s_data,'data':data})

def teacher(request):
    t_data = Teacher.objects.all()
    return render(request,'teacher.html',{'t_data':t_data})

def add_teacher(request):
     Eid=request.POST['Eid']
     Name=request.POST['name']
     Email=request.POST['email']
     Mobile=request.POST['contact']
     Joining_Date=request.POST['Joining_Date']
     Education=request.POST['Education']
     Experience=request.POST['Experience']
     Salary=request.POST['Salary']
     if Teacher.objects.filter(Name=Name).exists():
        messages.info(request,'Teacher already exists')
        return render(request,"teacher.html")
     elif Teacher.objects.filter(Email=Email).exists():
        messages.info(request,'Teacher already exists')
        return render(request,"teacher.html")
     else:
        Teacher.objects.create(Emp_Id=Eid,Name=Name,Email=Email,Mobile=Mobile,Joining_Date=Joining_Date,Education=Education,Expriance=Experience,Privies_salary=Salary)
        messages.success(request,'!!!!Successfully Added!!!!')
        t_data=Teacher.objects.all()
        return render(request,'teacher.html',{'t_data':t_data})

def update_teacher(request):
    t=Teacher()
    t.id = request.POST['uid']
    t.EID = request.POST['Eid']
    t.Name=request.POST['name']
    t.Email=request.POST['email']
    t.Mobile=request.POST['contact']
    t.Joining_Date=request.POST['Joining_Date']
    t.Education=request.POST['Education']
    t.Expriance =request.POST['Experience']
    t.Privies_salary=request.POST['Salary']
    t.save()
    t_data=Teacher.objects.all()
    return render(request,'teacher.html',{'t_data':t_data})

def delete_teacher(request):
    Eid=request.GET['Eid']
    Teacher.objects.get(id=Eid).delete()
    t_data=Teacher.objects.all()
    return render(request,'teacher.html',{'t_data':t_data,})

def lgout(request):
    auth.logout(request)
    return render(request,'login.html')

def update_teacher_page(request,uid):
    res = Teacher.objects.get(id=uid)
    return render(request, 'update_teacher.html', context={
        'stu': res,
    })

def update_student_page(request,uid):
    res = Student.objects.get(id=uid)
    data=Course.objects.all()
    return render(request, 'update_student.html', context={
        'stu': res,
        'data':data
    })
    

def update_course_page(request,uid):
    res = Course.objects.get(id=uid)
    return render(request, 'update_course.html', context={
        'stu': res,
    })