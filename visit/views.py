from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from jdatetime import datetime
from visit.models import *
from visit.forms import *

time_now = datetime.date(datetime.now())
patient = Patient.objects.all()
visit = Visit.objects.all()


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
    if request.user.profile.role == 2:
        patient_list = Patient.objects.all()
    elif request.user.profile.role == 1:
        patient_list = Patient.objects.filter(doctor__user_id=request.user.id).order_by('-visit__datetime')
    else:
        patient_list = []

    context = {
        'count': patient_list.__len__(),
        'count_visit': visit.__len__(),
        'date': time_now,
        'role': request.user.profile.role
    }
    return render(request, 'visit/main_page.html', context)


@login_required
def show_patient(request):
    if request.user.profile.role == 2:
        patient_list = Patient.objects.all()
    elif request.user.profile.role == 1:
        patient_list = Patient.objects.filter(doctor__user_id=request.user.id)
    else:
        patient_list = []

    search_form = SearchPatient(request.GET)
    if search_form.is_valid():
        patient_name = search_form.cleaned_data['patient_name']
        doctor_name = search_form.cleaned_data['doctor_name']
        national_id = search_form.cleaned_data['national_id']
        # begin_date = search_form.cleaned_data['begin_date']
        # end_date = search_form.cleaned_data['end_date']
        patient_list = patient_list.filter(fullname__contains=patient_name)
        patient_list = patient_list.filter(doctor__fullname__contains=doctor_name)
        patient_list = patient_list.filter(file_number__contains=national_id)
    else:
        patient_list = Patient.objects.all()

    context = {
        'patient': patient_list,
        'count': patient_list.__len__(),
        'date': time_now,
        'search_form': search_form
    }
    return render(request, 'visit/show_patient.html', context)


@login_required
def show_files(request):
    search_form = SearchPatient(request.GET)
    if search_form.is_valid():
        patient_name = search_form.cleaned_data['patient_name']
        doctor_name = search_form.cleaned_data['doctor_name']
        national_id = search_form.cleaned_data['national_id']
        # begin_date = search_form.cleaned_data['begin_date']
        # end_date = search_form.cleaned_data['end_date']
        visit_list = Visit.objects.filter(patient__file_number__contains=patient_name)
        visit_list = visit_list.filter(doctor__fullname__contains=doctor_name)
        visit_list = visit_list.filter(patient__file_number__contains=national_id)
    else:
        visit_list = Visit.objects.all()
    context = {
        'visit_list': visit_list,
        'count': visit_list.__len__(),
        'date': time_now,
        'search_form': search_form
    }
    return render(request, 'visit/show_files.html', context)


@login_required
def add_patient(request):
    add_form = AddPatientForm(request.POST)

    if request.method == 'POST':
        if add_form.is_valid:
            par = add_form.save(commit=False)
            par.save()
            messages.success(request, 'با موفقیت ثبت شد')
            return redirect('visit:main_page')
        else:
            messages.error(request, 'مشکلی رخ داده است')
            return redirect('visit:add_patient')
    else:
        context = {
            'add_form': add_form,
            'date': time_now
        }
        return render(request, 'visit/add_patient.html', context)


@login_required
def edit_info(request):
    edit_doctor = EditDoctorInformation(request.POST or None, instance=request.user.profile)
    if request.method == 'POST':
        if edit_doctor.is_valid:
            edit_doctor.save(commit=True)
            return redirect('visit:main_page')

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


@login_required
def add_doctor(request):
    if request.user.profile.role > 1:
        doctor_form = AddDoctor(request.POST)
        if request.method == 'POST':
            if doctor_form.is_valid:
                doctor_form.save()
                return redirect('visit:main_page')
        else:
            context = {
                'doctor_form': doctor_form,
                'date': time_now
            }
            return render(request, 'visit/add_doctor.html', context)
    else:
        return redirect('visit:main_page')


@login_required
def add_user(request):
    if request.user.profile.role > 1:
        user_form = AddUser(request.POST)
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            return redirect('visit:main_page')
        else:
            context = {
                'form': form,
                'date': time_now
            }
            return render(request, 'visit/add_user.html', context)
    else:
        return redirect('visit:main_page')


@login_required()
def patient_detail(request, fileNumber):
    patient_file = get_object_or_404(Patient, file_number=fileNumber)
    context = {
        'patient': patient_file,
        'date': time_now
    }
    return render(request, 'visit/patient_detail.html', context)


@login_required()
def visit_detail(request, visit_id):
    visit_file = get_object_or_404(Visit, pk=visit_id)
    context = {
        'visit': visit_file,
        'date': time_now
    }
    return render(request, 'visit/file_detail.html', context)
