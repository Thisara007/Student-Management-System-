from django import forms
from .models import student

class studentform(forms.ModelForm):
    class Meta:
        model=student
        fields="__all__"
        labels={"fname":"First Name",
                "lname":"Last Name",
                "regno":"Registration number",
                "register_date":"Register Date",
                "email":"Email",
                "branch":"Department"}
        
        widgets={
            "fname":forms.TextInput(attrs={"class":"form-control"}),
            "lname":forms.TextInput(attrs={"class":"form-control"}),
            "regno":forms.NumberInput(attrs={"class":"form-control"}),
            "email":forms.EmailInput(attrs={"class":"form-control"}),
            "branch":forms.Select(attrs={"class":"form-control"}),
            "register_date":forms.DateInput(attrs={"class":"form-control"})}
           
           
