from django.shortcuts import get_object_or_404,render
from employees.models import Employee
from django.http import HttpResponse

# Create your views here.
def employees_detail(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    context={
        'employee':employee
    }
    return render(request, 'employee_detail.html',context)