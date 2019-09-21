from django.shortcuts import render, redirect
from .models import *

# Create your views here.
def home(request):
    return render(request, 'index.html')

def upload(request):
    if request.method == 'POST':
        ti = Test_ins.objects.create()
        ti.nom = request.POST['nom']
        ti.prenom = request.POST['prenom']
        ti.email = request.POST['email']
        ti.image = request.FILES['image_profil']
        ti.save()
    redirect('home')