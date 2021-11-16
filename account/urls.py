from django.contrib import admin
from django.urls import path
from account.views import *

app_name = 'account'
urlpatterns = [
    path('login/', login_view, name='login_view'),
    path('logout/', logout_view, name='logout_view'),

]