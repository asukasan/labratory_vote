from django.shortcuts import render
from django.views.generic import ListView
from .models import Laboratory
from django.contrib.auth.mixins import LoginRequiredMixin

class LabsView(LoginRequiredMixin, ListView):
    model = Laboratory
    template_name = 'labs/laboratory.html'
    context_object_name = 'labs'
    
    
