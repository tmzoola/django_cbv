from django.urls import path
from .views import HomeView,ThankYouView,ContactFormView,TeacherCreateView

app_name = 'classroom'

urlpatterns = [
    path('home_view/',HomeView.as_view(), name='home_view'),
    path('thank_you/',ThankYouView.as_view(), name='thank_you'),
    path('contact/',ContactFormView.as_view(), name='contact'),
    path('teacher_form/',TeacherCreateView.as_view(), name='teacher_form'),
]