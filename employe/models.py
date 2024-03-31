from django.db import models
from curds.models import Curd

class EmployeeModel(models.Model):
   phoneno = models.CharField(max_length=15)
   job_description = models.CharField(max_length=100)
   bio = models.ForeignKey(Curd, on_delete=models.DO_NOTHING, default= True)

   class Meta:
        db_table = "employe"

class SalaryModel(models.Model):
       employee = models.ForeignKey(EmployeeModel, on_delete=models.DO_NOTHING, default=True)
       basic_sal = models.CharField(max_length=10)
       epf = models.CharField(max_length=10)
       net_sal = models.CharField(max_length=10)

       class Meta:
        db_table = "salary"