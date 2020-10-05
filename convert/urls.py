from django.urls import path
from . import views

urlpatterns = [

    path('word-to-pdf/', views.WordToPdf.as_view()),
]