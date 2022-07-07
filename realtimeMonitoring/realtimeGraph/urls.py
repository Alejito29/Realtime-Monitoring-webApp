from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from .views import *

urlpatterns = [
    path('', DashboardView.as_view(), name='dashboard'),
    path('getInformation/', DashboardView.as_view(), name='getInformation'),
    path('historical/', HistoricalView.as_view(), name='historical'),
]