from django.urls import path,include
from .views import *

urlpatterns=[
    path('employee/',EmployeeApiView.as_view()),
    path('salary/' ,SalaryApiview.as_view()),
    path('empdelete/<int:id>',DeleteEmployee.as_view()),
    path('saldelete/<int:id>',DeleteSalary.as_view())

]