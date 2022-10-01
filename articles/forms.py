from django import forms

from .models import *


class GuestForm(forms.Form):
    class Meta:
        class GuestForm(forms.Form):
            author= forms.CharField(max_length=200, required=True, label='Name')
            email = forms.EmailField(max_length=200, required=True, label='Email')
            # author = forms.CharField(max_length=10, required=True, label='Author')
            text = forms.CharField(max_length=2000,
                                   required=True,
                                   label='Text',
                                   widget=forms.Textarea)