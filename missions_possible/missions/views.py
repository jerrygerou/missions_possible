from django.shortcuts import render
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
