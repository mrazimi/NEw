from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from jdatetime import datetime

from visit.models import *
from visit.forms import *

time_now = datetime.date(datetime.now())


# Create your views here.
@login_required
def main_page(request):
    """    if request.user.profile.role == 0:
        pass
    elif request.user.profile.role == 1:
        pass
    elif request.user.profile.role == 2:
        pass
        """
    patient = Patient.objects.all()
    context = {
        'count': patient.__len__(),
        'date': time_now,
        'role': request.user.profile.role
    }
    return render(request, 'visit/main_page.html', context)


@login_required
def show_patient(request):
    patient = Patient.objects.all()
    context = {
        'patient': patient,
        'count': patient.__len__(),
        'date': time_now
    }
    return render(request, 'visit/show_patient.html', context)


@login_required
def add_patient(request):
    if request.method == 'POST':
        add_form = AddPatientForm(request.POST)
        if add_form.is_valid():
            add_form.save()
            messages.success(request, 'با موفقیت ثبت شد')
        else:
            messages.error(request, 'مشکلی رخ داده است')
        return redirect('visit:add_patient')
    else:
        add_form = AddPatientForm()

    context = {
        'add_form': add_form,
        'date': time_now
    }
    return render(request, 'visit/add_patient.html', context)


@login_required
def edit_info(request):
    edit_doctor = EditDoctorInformation(instance=request.user.profile)
    context = {
        'edit_doctor': edit_doctor,
        'date': time_now
    }
    return render(request, 'visit/edit_info.html', context)


@login_required
def add_doc(request):
    if request.method == 'POST':
        add_document_form = AddDocument(request.POST)
        if add_document_form.is_valid():
            doc = add_document_form.save(commit=False)
            doc.profile = request.user.profile
            doc.save()
            messages.success(request, 'با موفقیت ثبت شد')
        else:
            messages.error(request, 'مشکلی رخ داده است')
        return redirect('visit:add_doc')
    else:
        add_document_form = AddDocument()
    context = {
        'add_document_form': add_document_form,
        'date': time_now
    }
    return render(request, 'visit/add_doc.html', context)
