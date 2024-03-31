from django.contrib import admin

from .models import EmployeeModel,SalaryModel

admin.site.register(EmployeeModel)
admin.site.register(SalaryModel)
