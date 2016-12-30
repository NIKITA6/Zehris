from django.db import models

class Employee(models.Model):
    fname = models.CharField(max_length=200)
    lname = models.CharField(max_length=200)
    pwd = models.CharField(max_length=200)
    SnapHost_Calendar = models.DateTimeField()
    email = models.CharField(max_length=200)
    emp_no = models.IntegerField(default=0)
    earn_apply_leave = models.IntegerField(default=0)
    sic_apply_leave = models.IntegerField(default=0)
    earn_leave = models.IntegerField(default=0)
    sick_leave = models.IntegerField(default=0)
    mob = models.IntegerField(default=0)
    address = models.CharField(max_length=200)
    postcode = models.IntegerField(default=0)
    
    
