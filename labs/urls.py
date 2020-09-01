from django.urls import path
from .views import LabsView

urlpatterns = [
    path('labs/', LabsView.as_view(), name='labs'),
]
