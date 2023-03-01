from django.shortcuts import render
from django.http import HttpResponse

from django.views.generic import TemplateView,FormView
from .forms import ContactForm



class HomeView(TemplateView):
    template_name = 'classroom/home.html'

class ThankYouView(TemplateView):
    template_name = 'classroom/thank_you.html'


class ContactFormView(FormView):
    form_class = ContactForm
    template_name = 'classroom/contact.html'

    success_url = "/classroom/thank_you"

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)