from django.shortcuts import render
from django.views import View


class MainView(View):
    def get(self, request):
        return render(request, 'main.html')


class AboutUs(View):
    def get(self, request):
        return render(request, 'about_us.html')


class Contacts(View):
    def get(self, request):
        return render(request, 'contacts.html')
