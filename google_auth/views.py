from django.shortcuts import render
from django.http import HttpResponse


def successfully_login(request):
    return HttpResponse(f'{ request.user.first_name } {request.user.last_name} you are successfully login')
