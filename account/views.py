from django.shortcuts import render
from django.contrib.auth.models import User


def doctor_list(request):
    doctors = User.objects.all()
    return render(request, 'user/doctor_list.html', {
        'doctors': doctors
    })

# Create your views here.
