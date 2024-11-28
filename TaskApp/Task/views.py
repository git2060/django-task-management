from django.shortcuts import render, redirect, get_object_or_404
from .models import TaskModel
from .forms import TaskForm
# Create your views here.


def view_task(request):
    if request.method=="POST":
        val = request.POST.get('value','')
        data=TaskModel.objects.filter(name__icontains=val)
    else:
        data=TaskModel.objects.all()
    return render(request, "task/view_task.html", {"data":data})



def add_task(request):
    if request.method=="POST":
        form=TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_task')
    else:
        form=TaskForm()
    return render(request,"task/add_edit_task.html",{"form":form})  



def edit_task(request,pk): 
    data= get_object_or_404(TaskModel,pk=pk)
    if request.method=="POST":
        form=TaskForm(request.POST,instance=data)
        if form.is_valid():
            form.save()
            return redirect('view_task')
    else:
        form=TaskForm(instance=data)
    return render(request,"task/add_edit_task.html",{"form":form}) 



def delete_task(request,pk): 
    data= get_object_or_404(TaskModel,pk=pk)
    if request.method=="POST":
        data.delete()
        return redirect('view_task')
    return render(request,"task/delete_task.html",{"data":data}) 

def update_task(request,pk):
    data= get_object_or_404(TaskModel,pk=pk)
    if request.method=="GET":
        if data.is_completed==True:
            data.is_completed=False
        else:
            data.is_completed=True
        data.save() 
    return redirect('view_task')       