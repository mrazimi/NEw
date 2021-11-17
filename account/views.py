from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse


def login_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('visit:main_page'))
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is None:
                context = {
                    'username': username,
                    'error_text': 'کاربری با این مشخصات یافت نشد'
                }
                return render(request, "account/login_page.html", context)
            else:
                login(request, user)
                return HttpResponseRedirect(reverse('visit:main_page'))
        else:
            context = {}
            return render(request, "account/login_page.html", context)


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('account:login_view'))
