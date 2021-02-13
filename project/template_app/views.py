from django.shortcuts import render
from template_app.models import Employee
from template_app.forms import EmployeeForm
from django.shortcuts import redirect

# Create your views here.
def index(request):
    return render(request, 'template_app/index.html')


def aboutus(request):
    return render(request, 'template_app/about_us.html')

def contactus(request):
    return render(request, 'template_app/contact_us.html')

def employee(request):
    form = EmployeeForm()
    print("Request came")
    
    print(request.method)
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        print(form.errors)
        if form.is_valid():
            try:
                form.save()
                return redirect('/employee/list')
            except Exception as ex:
               
                print("Exception", ex)
    
    return render(request, 'template_app/employee.html',{'form':form})

def employee_list(request):
    data = {'employees': Employee.objects.all()}
    return render(request, 'template_app/employee-list.html',data)
