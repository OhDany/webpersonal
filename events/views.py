from django.shortcuts import render
from .models import Project

# Create your views here.
def events(request):
    projects = Project.objects.all()
    return render(request, 'events/events.html', {'projects':projects})
