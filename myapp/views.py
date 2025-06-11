from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    str_html = "<h1>My App</h1>"
    return HttpResponse(str_html)

def index(request):
    context ={
        'title':'PU college'
    }
    return render(request,'index.html',context)

def add_student(request):
    context={'msg':'New Student'}
    if request.method=='GET':
        unm=request.GET.get("unm")
        prog=request.GET.get("prog")
        sec=request.GET.get("sec")
        

        print(f'Name{request.GET.get("unm")}')
        if unm != '' and unm != None:
            from .models import Student
            s1 = Student()
            s1.unm = unm
            s1.prog = prog
            s1.sec = sec
            s1.save
            context={'msg':'Student Info Saved'}
    return render(request,'add_student.html',context)

def display_students(request):
    print('in display')
    from .models import Student
    studs = Student.objects.all()
    print(stu)
    context = {'studs':studs}
    return render(request,'display_students.html', context)

def delete_student(request,id):
    from .models import Student
    s = Student.objects.get(id=id)
    s.delete()
    studs = Student.objects.all()
    context = {'studs':studs}
    return render(request,'display_students.html', context)

def update_student(request,id):
    from .models import Student
    stud = Student.objects.get(id=id)
    msg = 'Make changes to update'
    if request.method=='POST':
       unm = request.POST.get('unm')
       prog = request.POST.get('prog')
       sec = request.POST.get('sec')

       stud.unm = unm
       stud.prog = prog
       stud.sec = sec
       stud.save()
       msg ='Updated...' 
       ''
    context = {'stud':stud,'msg':msg}
    return render(request,'update_student.html',context)


