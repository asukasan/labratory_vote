from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, Profile, Inquiry
from labs.models import Laboratory
from django.db import transaction
from django.forms.utils import ValidationError

class SignUpForm(UserCreationForm):
    belongs1 = forms.ModelChoiceField(queryset=Laboratory.objects.all(), label='第一希望',)
    belongs2 = forms.ModelChoiceField(queryset=Laboratory.objects.all(), label='第二希望',)
    belongs3 = forms.ModelChoiceField(queryset=Laboratory.objects.all(), label='第三希望',)
    rank = forms.IntegerField(widget=forms.NumberInput, required=True, label='順位')
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('num',)
 

    @transaction.atomic
    def save(self):
        user = super().save()
        belongs1 = self.cleaned_data.get('belongs1')
        belongs2 = self.cleaned_data.get('belongs2')
        belongs3 = self.cleaned_data.get('belongs3')
        rank = self.cleaned_data.get('rank')
        profile = Profile.objects.create(user=user, belongs1=belongs1, belongs2=belongs2, belongs3=belongs3, rank=rank)
        return user
  

class InquiryForm(forms.ModelForm):
    class Meta:
        model = Inquiry
        fields = ('text',)
        widgets = {
            'text': forms.Textarea,
        }

class LoginForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('num', 'password')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['num'].widget = forms.
        for field_name, field in self.fields.items():
            # field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = field.label
          