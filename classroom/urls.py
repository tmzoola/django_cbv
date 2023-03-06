from django.urls import path
from .views import HomeView,ThankYouView,ContactFormView,TeacherCreateView,TeacherListView,TeacherDetailView

app_name = 'classroom'

urlpatterns = [
    path('home_view/',HomeView.as_view(), name='home_view'),
    path('thank_you/',ThankYouView.as_view(), name='thank_you'),
    path('contact/',ContactFormView.as_view(), name='contact'),
    path('teacher_form/',TeacherCreateView.as_view(), name='teacher_form'),
    path('teacher_list/',TeacherListView.as_view(), name='teacher_list'),
    path('teacher_detail/<int:pk>',TeacherDetailView.as_view(),name='teacher_detail')
]