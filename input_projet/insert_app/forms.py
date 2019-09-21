from django import forms
from .models import *

class Test_ins(forms.Form):
    class Meta:
        model= Test_ins
        fields = ('nom', 'prenom', 'email', 'image')