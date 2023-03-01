from django.shortcuts import render
from django.http import HttpResponse

from django.views.generic import TemplateView




class HomeView(TemplateView):
    template_name = 'classroom/home.html'

class ThankYouView(TemplateView):
    template_name = 'classroom/thank_you.html'