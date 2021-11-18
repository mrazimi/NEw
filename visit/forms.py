from django import forms
from django.contrib.admin.widgets import AdminDateWidget, AdminSplitDateTime, ForeignKeyRawIdWidget, AdminTimeWidget
from django.forms import DateInput, SelectDateWidget
import account.models
from visit.models import *
from account.models import *
from django.contrib.admin import widgets


class SearchPatient(forms.Form):
    patient_name = forms.CharField(max_length=100, required=False, label='نام بیمار')
    doctor_name = forms.CharField(max_length=100, required=False, label='نام دکتر معالج')
    begin_date = forms.DateTimeField(label='از تاریخ', required=False, widget=SelectDateWidget)
    end_date = forms.DateTimeField(label='تا تاریخ', required=False, widget=SelectDateWidget)


class AddPatientForm(forms.ModelForm):
    age = forms.DateTimeField(label='سن', required=False, widget=SelectDateWidget)

    class Meta:
        model = Patient
        fields='__all__'
        #exclude = ['doctor']


class EditDoctorInformation(forms.ModelForm):
    class Meta:
        model = profile
        exclude = ['user', 'role']


class AddDocument(forms.ModelForm):
    datetime = forms.DateField(label='زمان مراجعه', required=False, widget=AdminSplitDateTime)

    class Meta:
        model = Visit
        fields = '__all__'
        widgets = {
            'datetime': AdminDateWidget(),
        }


class AddUser(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'


class AddDoctor(forms.ModelForm):
    class Meta:
        model = profile
        fields = '__all__'
