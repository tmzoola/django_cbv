from django.shortcuts import render
from django.http import HttpResponse
from classroom.models import Teacher

from django.views.generic import TemplateView,FormView,CreateView,ListView,DetailView,UpdateView,DeleteView
from .forms import ContactForm



class HomeView(TemplateView):
    template_name = 'classroom/home.html'

class ThankYouView(TemplateView):
    template_name = 'classroom/thank_you.html'


class TeacherCreateView(CreateView):
    model = Teacher
    fields = "__all__"
    
    success_url = "/classroom/thank_you"


class TeacherListView(ListView):
    model = Teacher
    context_object_name = "teacher_list"

class TeacherDetailView(DetailView):
    #model_detail.html
    model = Teacher
 

 #Update View
class TeacherUpdateView(UpdateView):
    model = Teacher
    fields = "__all__"
    success_url = "/classroom/teacher_list"


class TeacherDeleteView(DeleteView):
    model = Teacher
    success_url = "/classroom/teacher_list"






class ContactFormView(FormView):
    form_class = ContactForm
    template_name = 'classroom/contact.html'

    success_url = "/classroom/thank_you"

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)