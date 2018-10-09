from django.contrib import messages
from django.shortcuts import render
from django.urls import reverse
from django.views import generic

from .models import Mission, OpenEndedQuestion, RatingQuestion, OpenEndedAnswer, RatingAnswer


class MissionIndexView(generic.ListView):
    """
    A view to display all existing missions.
    """
    template_name = 'missions/index.html'
    context_object_name = 'mission_list'

    def get_queryset(self):
        return Mission.objects.all()


class MissionCreateView(generic.CreateView):
    """
    A view for user to create a mission from a form. Redirect to index with success message.
    """
    model = Mission
    template_name = 'missions/add_mission.html'
    fields = ['name', 'description']

    def get_success_url(self):
        messages.success(self.request, 'A new mission has been created!')
        return reverse('missions:index')


class MissionDetailView(generic.DetailView):
    """
    View all questions and associated answers in a mission.
    """
    model = Mission
    template_name = 'missions/mission_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        mission = self.object
        context['open_ended_questions'] = OpenEndedQuestion.objects.filter(mission_id=mission.id)
        return context


class OpenEndedQuestionCreateView(generic.CreateView):
    model = OpenEndedQuestion
    fields = ['text', 'mission']
    template_name = 'missions/add_question.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['mission_id'] = self.kwargs['mission_id']
        return context

    def get_success_url(self):
        messages.success(self.request, 'A new question has been added!')
        return reverse('missions:mission_detail', kwargs={'pk': self.kwargs['mission_id']})
