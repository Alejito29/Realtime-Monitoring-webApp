from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from .views import *

urlpatterns = [
    path('aaaaaaa', TestData.as_view(), name='getTestData'),
    path('historical/', HistoricalView.as_view(), name='historical'),
]