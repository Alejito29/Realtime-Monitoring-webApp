from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from .views import *

urlpatterns = [
    path('', DashboardView.as_view(), name='dashboard'),
    path('getTest/', name='getTestData'),
    path('historical/', HistoricalView.as_view(), name='historical'),
]