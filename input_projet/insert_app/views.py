from django.shortcuts import render, redirect
from django.core.validators import validate_email
from .models import *
from . import forms
# Create your views here.
def home(request):
    return render(request, 'index.html')

def upload(request):
    if request.method == 'POST':
        ti = Test_ins(
            nom = request.POST['nom'],
            prenom = request.POST['prenom'],
            email = request.POST['email'],
        )
        ti.save()
    return redirect('home')


def profile(request):
    return render(request, 'home.html')


def profile_upload(request):
    if request.method == 'POST':
        is_email = False
        try:
            validate_email(request.POST['email'])
            is_email = True
        except:
            pass
        if is_email and request.POST['nom'] and request.POST['prenom']:
            ti = Test_ins(
                nom = request.POST['nom'],
                prenom = request.POST['prenom'],
                email = request.POST['email'],
                image = request.FILES['image'],
            )
            ti.save()
        # test=forms.Test_ins(request.POST,request.FILES)
        # test.save()
    return redirect('profile')