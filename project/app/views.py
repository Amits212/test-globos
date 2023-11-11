from django.shortcuts import render
from .models import State

def get_world(request):
    return render(request, 'world.html')


def get_all_states(request):
    states = State.objects.all()
    return render(request, 'index.html', {'states':states})