from django import forms
from django.contrib.admin.widgets import AdminDateWidget, AdminSplitDateTime, ForeignKeyRawIdWidget, AdminTimeWidget
from django.forms import DateInput, SelectDateWidget
import account.models
from visit.models import *
from account.models import *
from django.contrib.admin import widgets


class AddPatientForm(forms.ModelForm):
    age = forms.DateTimeField(label='سن', required=False, widget=SelectDateWidget)

    class Meta:
        model = Patient
        fields = ['file_number', 'fullname', 'age', 'phone']


class EditDoctorInformation(forms.ModelForm):
    class Meta:
        model = profile
        exclude = ['user']


class AddDocument(forms.ModelForm):
    datetime = forms.DateField(label='زمان مراجعه', required=False, widget=AdminSplitDateTime)

    class Meta:
        model = Visit
        exclude = ['doctor']
        widgets = {
            'datetime': AdminDateWidget(),
        }

