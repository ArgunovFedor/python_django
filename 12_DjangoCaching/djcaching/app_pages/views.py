from django.shortcuts import render
from time import sleep

def welcome(request, *args, **kwargs):
    sleep(4)
    return render(request, 'app_pages/welcome.html')

def main_page(request, *args, **kwargs):
    return render(request, 'app_pages/main.html')