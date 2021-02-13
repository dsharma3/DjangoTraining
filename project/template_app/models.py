from django.db import models

# Create your models here.
class Employee(models.Model):
    employee_id = models.CharField(max_length=50, unique = True)    
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField()
    contact_number = models.IntegerField()

    class Meta:
        db_table = 'Employee'