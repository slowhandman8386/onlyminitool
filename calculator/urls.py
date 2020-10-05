from django.urls import path
from . import views

urlpatterns = [

    path('fd/', views.FixDeposit.as_view(), name='fd'),
    path('car-load/', views.CarLoan.as_view(), name='car-load'),
    path('home-load/', views.HomeLoan.as_view(), name='home-load'),
    path('bmi/', views.Bmi.as_view(), name='bmi'),
]