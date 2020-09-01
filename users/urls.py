from django.urls import path
from .views import ProfileView, InquiryView

urlpatterns = [
    path('profile/', ProfileView.as_view(), name='profile'),
    path('inquiry/', InquiryView.as_view(), name='inquiry'),
]
