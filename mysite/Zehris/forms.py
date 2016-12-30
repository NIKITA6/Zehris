from django import forms
from Zehris.models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model=Employee
        exclude=()