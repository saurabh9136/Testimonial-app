from django.shortcuts import render, redirect
from django.http import HttpResponse

from emp.forms import FeedbackForm
from emp.models import Emp, Feedback
from testimonial.models import Testimonial

# Create your views here.

def emp_home(request):
    emp_data = Emp.objects.all() #return all data
    print(" all data fetched ")
    return render(request, 'emp/home.html', {
        'emps' : emp_data
    })

def delete_emp(request, id):
    emp_data = Emp.objects.get(pk = id)
    emp_data.delete()
    print("Data deleted successfully")
    return redirect("/emp/home/")

def update_emp(request, id) :
    emp_data = Emp.objects.get(pk = id)
    print("Update function called")
    return render(request,"emp/update-emp.html", {
        "emp":emp_data})

def do_update_emp(request, id):
    if request.method == "POST" :

        emp_name = request.POST.get("emp_name")
        emp_id_temp = request.POST.get("emp_id")
        emp_phone = request.POST.get("emp_phone")
        emp_address = request.POST.get("emp_address")
        emp_working = request.POST.get("emp_working")
        emp_dept = request.POST.get("emp_dept")

        e = Emp.objects.get(pk=id)
        e.name = emp_name
        e.emp_id = emp_id_temp
        e.phone = emp_phone
        e.address = emp_address
        e.department = emp_dept

        if emp_working is None :
            e.working = False
        else:
            e.working = True
        e.save()

        print("Data updated successfully")
        return redirect('/emp/home')

def add_emp(request):
    if request.method == "POST" :
        emp_name = request.POST.get("emp_name")
        emp_id = request.POST.get("emp_id")
        emp_phone = request.POST.get("emp_phone")
        emp_address = request.POST.get("emp_address")
        emp_working = request.POST.get("emp_working")
        emp_dept = request.POST.get("emp_dept")

        e = Emp()
        e.name = emp_name
        e.emp_id = emp_id
        e.phone = emp_phone
        e.address = emp_address
        e.department = emp_dept

        if emp_working is None :
            e.working = False
        else:
            e.working = True

        e.save()
        print("Data created successfully")
        return redirect("/emp/home/")
    
    return render(request, "emp/add_emp.html", {})

def testimonials_data(request):

    data = Testimonial.objects.all()
    return render(request, "emp/testimonial.html", {
        "test_data" : data
    })
def feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)

        if form.is_valid():
            obj = Feedback()
            obj.name = form.cleaned_data['name']
            obj.email = form.cleaned_data['email']
            obj.feed = form.cleaned_data['feedback']
            obj.save()
            print("data saved by feedback")
        else :
            return render(request, "emp/feedback.html", {'form' : form})
    else :
        form = FeedbackForm(request.POST)
        return render(request, "emp/feedback.html", {'form' : form})
    
    