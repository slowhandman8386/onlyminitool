from django.urls import path
from . import views

urlpatterns = [

    path('dig/', views.Dig.as_view(), name='dig'),
    path('ip/', views.Ip.as_view(), name='ip'),
    path('whois/', views.WhoIs.as_view(), name='whois'),
    path('check-port/', views.IpCheckPort.as_view(), name='checkport'),
]