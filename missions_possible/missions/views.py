from django.contrib import messages
from django.shortcuts import render
from django.urls import reverse
from django.views import generic

from .models import Mission


class MissionIndexView(generic.ListView):
    """
    A view to display all existing missions.
    """
    template_name = 'missions/index.html'
    context_object_name = 'mission_list'

    def get_queryset(self):
        return Mission.objects.all()


class MissionCreateView(generic.CreateView):
    model = Mission
    template_name = 'missions/add_mission.html'
    fields = ['name', 'description']

    def get_success_url(self):
        messages.success(self.request, 'A new mission has been created!')
        return reverse('missions:index')
