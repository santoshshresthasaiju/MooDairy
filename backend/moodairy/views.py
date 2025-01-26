from django.shortcuts import redirect, render, get_object_or_404
from .forms import EmployeeForm
from .models import Employee
from django.contrib import messages
# Create your views here.
def employee_create(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm()
    context ={
        'form':form,
        'title':'Add Employee'
    }
    return render(request, 'moodairy/employee_form.html', context)

def employee_update(request, emp_id):
    emp = get_object_or_404(Employee, id=emp_id)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=emp)
        if form.is_valid():
            form.save()
            messages.success(request, 'Updated Successfully!')
    else:   
        form = EmployeeForm(instance=emp)
    context ={
        'form':form,
        'title':'Update Employee'
    }
    return render(request, 'moodairy/employee_form.html', context)

