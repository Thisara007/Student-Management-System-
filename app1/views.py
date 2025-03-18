from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import student
from .forms import studentform
from django.db.models import Q

# Create your views here.
def index(request):
    data=student.objects.values()
    return render(request,"index.html",{"data":data})

def enter(request):
    if request.method=="POST":
        form=studentform(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")
    else:
        form=studentform()
    return render(request,"form.html",{"data":form})

def update(request,id):
    if request.method=="POST":
        data=student.objects.get(pk=id)
        form=studentform(request.POST,instance=data)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")
    else:
        data=student.objects.get(pk=id)
        form=studentform(instance=data)
        return render(request,"form.html",{"data":form})
    
def delete(request,id):
    if request.method=="POST":
        data=student.objects.get(pk=id)
        data.delete()
        return HttpResponseRedirect("/")
def search(request):
    if  request.method=="POST":
        search=request.POST.get("output")
        all_students=student.objects.all()
        if search:
            std=all_students.filter(
                Q(fname__icontains=search)|
                 Q(lname__icontains=search)|
                  Q(regno__icontains=search)|
                   Q(register_date__icontains=search)|
                    Q(email__icontains=search)|
                     Q(branch__icontains=search))
            return render (request,"index.html",{"data":std})
        else:
            return  HttpResponseRedirect("/")
            
    else:
       return HttpResponse("No such data") 
                            