
from urllib import response
from django.http import HttpResponseRedirect
from django.shortcuts import render
from testapp import models


def deco_login(f1):
    def mod_f1(request):
        if 'username' in request.session.keys():
            return f1(request)    
        else:  
            return HttpResponseRedirect("http://localhost:8000/testapp/login/")
    return mod_f1
def userLogout(request):
    del request.session['username']
    return HttpResponseRedirect("http://localhost:8000/testapp/login/")
def loginValidate(request):
    username=request.POST['username']
    password=request.POST['password']
    try:
        user=models.Testapp_User.objects.get(username=username,password=password)
        s="http://localhost:8000/testapp/View-employee/"
        request.session['username']=username
    except:
        s="http://localhost:8000/testapp/login/"  
    return HttpResponseRedirect(s)      
def userLogin(request):
    res=render(request,'testapp/user_login.html')
    return res
def newUser(request):
    error_msg="Username Already Taken"
    d={}
    try:
        if int(request.GET['err'])==1:

            d['error_msg']=error_msg
    except:
        pass
    res = render(request,'testapp/new_user.html',d)
    return res
def userRegistration(request):
    myuser=models.Testapp_User()
    myuser.username=request.POST['username']
    try:
        if myuser==models.Testapp_User.objects.get(username=myuser.username):
            s="http://localhost:8000/testapp/new-user?err=1"
            return HttpResponseRedirect(s)
    except:
        pass        
    myuser.password=request.POST['password']
    myuser.save()
    return HttpResponseRedirect("http://localhost:8000/testapp/login/")
def deleteAdvance(request):
    adv=models.advanceForm.objects.get(id=request.GET['id'])
    adv.delete()
    return HttpResponseRedirect('http://localhost:8000/testapp/View-advance/') 
@deco_login    
def updateAdvance(request):
    adv=models.advanceForm.objects.get(id=request.GET['id'])
    res = render(request,'testapp/update_advance.html',{'adv':adv,})
    return res
def updationAdvance(request):
    emp=models.newEmployee()
    emp.id=request.POST['id']
    emp.eno=request.POST['eno']
    emp.ename=request.POST['ename']
    emp.bdate=request.POST['erole']
    emp.eaddress=request.POST['edate']
    emp.estate=request.POST['eadvance']
    emp.save()
    return HttpResponseRedirect('http://localhost:8000/testapp/View-advance/') 
@deco_login       
def viewAdvance(request):
    employees = models.advanceForm.objects.all()
    d = {'employees':employees,}
    response = render(request,'testapp/view_advance.html',d)
    return response
def saveAdvance(request):
    adv = models.advanceForm()
    adv.eno = request.POST['eno']
    adv.ename = request.POST['ename']
    adv.erole = request.POST['erole']
    adv.edate = request.POST['edate']
    adv.eadvance = request.POST['eadvance']
    adv.save()
    return HttpResponseRedirect('http://localhost:8000/testapp/View-advance/')
@deco_login    
def advance(request):
    response = render(request,'testapp/advance.html')
    return response


def viewSalary(request):
    esalary = models.salaryForm.objects.all()
    d = {'esalary':esalary}
    response = render(request,'testapp/view_salary.html',d)
    return response
def Save(request):
    sal = models.salaryForm()
    sal.eno=request.POST['eno']
    sal.ename=request.POST['ename']
    sal.emonth=request.POST['emonth']
    sal.edate=request.POST['edate']
    sal.erole=request.POST['erole']
    sal.ebasic=request.POST['ebasic']
    sal.epf=request.POST['epf']
    sal.eadvance=request.POST['eadvance']
    sal.enet=request.POST['enet']
    sal.save()
    return HttpResponseRedirect("http://localhost:8000/testapp/view-salary/")
@deco_login    
def salary(request):
    response = render(request,'testapp/salary.html')
    return response    

def deleteEmployee(request):
    emp=models.newEmployee.objects.get(id=request.GET['id'])
    emp.delete()
    return HttpResponseRedirect('http://localhost:8000/testapp/View-employee/')
@deco_login
def updateEmployee(request):
    emp=models.newEmployee.objects.get(id=request.GET['id'])
    res = render(request,'testapp/update_employee.html',{'emp':emp})
    return res
def updation(request):
    emp=models.newEmployee()
    emp.id=request.POST['id']
    emp.eno=request.POST['eno']
    emp.ename=request.POST['ename']
    emp.bdate=request.POST['bdate']
    emp.eaddress=request.POST['eaddress']
    emp.estate=request.POST['estate']
    emp.enum=request.POST['enum']
    emp.erole=request.POST['erole']
    emp.esal=request.POST['esal']
    emp.ejoin=request.POST['ejoin']
    emp.save()
    return HttpResponseRedirect('http://localhost:8000/testapp/View-employee/')
@deco_login    
def newEmployee(request):
    res = render(request,'testapp/new_employee.html')
    return res
def saveEmployee(request):
    emp=models.newEmployee()
    emp.eno=request.POST['eno']
    emp.ename=request.POST['ename']
    emp.bdate=request.POST['bdate']
    emp.eaddress=request.POST['eaddress']
    emp.estate=request.POST['estate']
    emp.enum=request.POST['enum']
    emp.erole=request.POST['erole']
    emp.esal=request.POST['esal']
    emp.ejoin=request.POST['ejoin']
    emp.save()
    return HttpResponseRedirect('http://localhost:8000/testapp/View-employee/')
@deco_login
def land(request):
    response = render(request,'testapp/test.html')
    return response
@deco_login    
def about(request):
    employees = models.newEmployee.objects.all()
    d = {'employees':employees,}
    response = render(request,'testapp/test1.html',d)
    return response
@deco_login
def contact(request):
    response = render(request,'testapp/test2.html')
    return response
