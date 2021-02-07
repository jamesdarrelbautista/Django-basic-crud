from django.shortcuts import render, redirect, get_object_or_404
from students.forms import StudentsForm
from students.models import Students

#from . import forms #(not sure if this works.. just comment or uncomment)
#from . import models #(not sure if this works.. just comment or uncomment)

# Create your views here.
def std(request):
    if request.method == "POST":
        form = StudentsForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/view')
            except:
                pass
    else:
        form = StudentsForm()
    return render(request,"students/index.html",{
        "form": form
    })

def view(request):
    students = Students.objects.all()
    return render(request, "students/view.html",{
        'students': students
    })


def delete(request, id):
    students = Students.objects.get(id=id)
    students.delete()
    return redirect("/view")

def edit(request, id):
    students = Students.objects.get(id=id)
    
    return render(request, "students/edit.html",{
        "students": students
    })

def update(request, id):

        student = get_object_or_404(Students, id=id)

        if request.method == 'GET':
                form = StudentsForm(instance=student)
                return redirect("/view")

        else:
                form = StudentsForm(request.POST, instance=student)
                form.save()
                return redirect("/view")
