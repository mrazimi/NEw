from django.contrib import admin
from django.urls import path
from visit.views import *
from django.views.i18n import JavaScriptCatalog

app_name = 'visit'
urlpatterns = [
    path('', main_page, name='main_page'),
    path('jsi18n', JavaScriptCatalog.as_view, name='js-catalog'),
    path('patient/', show_patient, name='show_patient'),
    path('add/', add_patient, name='add_patient'),
    path('editDoctorInfo/', edit_info, name='edit_info'),
    path('addDocument/', add_doc, name='add_doc'),
    path('addUser/', add_user, name='add_user'),
    path('addDoctor/', add_doctor, name='add_doctor'),
]