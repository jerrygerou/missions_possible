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
        context['rating_questions'] = RatingQuestion.objects.filter(mission_id=mission.id)
        context['open_ended_questions'] = OpenEndedQuestion.objects.filter(mission_id=mission.id)
        return context


class OpenEndedQuestionCreateView(generic.CreateView):
    model = OpenEndedQuestion
    fields = ['mission', 'text']
    template_name = 'missions/add_question.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['mission_id'] = self.kwargs['mission_id']
        return context

    def get_success_url(self):
        messages.success(self.request, 'A new question has been added!')
        return reverse('missions:mission_detail', kwargs={'pk': self.kwargs['mission_id']})


class RatingQuestionCreateView(generic.CreateView):
    model = RatingQuestion
    fields = ['mission', 'text']
    template_name = 'missions/add_rating_question.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['mission_id'] = self.kwargs['mission_id']
        return context

    def get_success_url(self):
        messages.success(self.request, 'A new rating question has been added!')
        return reverse('missions:mission_detail', kwargs={'pk': self.kwargs['mission_id']})


class OpenEndedAnswerCreateView(generic.CreateView):
    model = OpenEndedAnswer
    fields = ['question', 'response', 'user']
    template_name = 'missions/add_answer.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        question = OpenEndedQuestion.objects.get(id=self.kwargs['question_id'])
        context['user_id'] = self.request.user.id
        context['question_id'] = question.id
        context['question_text'] = question.text
        context['mission_id'] = question.mission.id
        return context

    def get_success_url(self):
        messages.success(self.request, 'Your answer was successfully submitted.')
        mission_id = OpenEndedQuestion.objects.get(id=self.kwargs['question_id']).mission.id
        return reverse('missions:mission_detail', kwargs={'pk': mission_id})


class RatingAnswerCreateView(generic.CreateView):
    model = RatingAnswer
    fields = ['question', 'response', 'user']
    template_name = 'missions/add_rating_answer.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        question = RatingQuestion.objects.get(id=self.kwargs['question_id'])
        context['user_id'] = self.request.user.id
        context['question_id'] = question.id
        context['question_text'] = question.text
        context['mission_id'] = question.mission.id
        return context

    def get_success_url(self):
        messages.success(self.request, 'Your answer was successfully submitted.')
        mission_id = RatingQuestion.objects.get(id=self.kwargs['question_id']).mission.id
        return reverse('missions:mission_detail', kwargs={'pk': mission_id})
