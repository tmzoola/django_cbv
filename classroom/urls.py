from django.urls import path
from .views import HomeView,ThankYouView

app_name = 'classroom'

urlpatterns = [
    path('home_view/',HomeView.as_view(), name='home_view'),
    path('thank_you/',ThankYouView.as_view(), name='thank_you'),
]