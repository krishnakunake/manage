from django.urls import path
from testapp.views import *

urlpatterns = [
    path('delete-advance/',deleteAdvance),
    path('update-advance/',updateAdvance),
    path('updation-advance/',updationAdvance),
    path('View-advance/',viewAdvance),
    path('saveadvance/',saveAdvance),
    path('advance/',advance),
    path('view-salary/',viewSalary),
    path('save-salary/',Save),
    path('salary/',salary),
    path('logout/',userLogout),
    path('login-validate',loginValidate),
    path('login/',userLogin),
    path('new-user',newUser),
    path('signup',userRegistration),
    path('delete-employee/',deleteEmployee),
    path('updation/',updation),
    path('update-employee/',updateEmployee),
    path('save-employee/',saveEmployee),
    path('new-employee/',newEmployee),      
    path('View-employee/',about),
    path('contact/',contact),
    
]