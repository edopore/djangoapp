from django import forms
from django.db.models import fields
from django.db.models.fields import PositiveBigIntegerField
from .models import *



class mikrotikForm(forms.ModelForm):
    class Meta:
        model = mikrotik
        fields = [
            'name',
            'host'
        ]

class userForm(forms.ModelForm):
    class Meta:
        model = user
        fields = [
            'fname',
            'lname'
        ]

class adminForm(forms.ModelForm):
    class Meta:
        model = administrator
        fields = [
            'email',
            'password',
        ]