from django.test import TestCase
from django.contrib.auth.models import User

from .models import Mission, OpenEndedQuestion, RatingQuestion, OpenEndedAnswer, RatingAnswer


class MissionModelTest(TestCase):
    def test_create_mission(self, name='Test Name', description='Some kind of description'):
        mission = Mission.objects.create(name=name, description=description)
        self.assertEqual(str(mission), mission.name)


class QuestionModelTests(TestCase):
    def test_create_open_ended_question(self):
        """
        Test creation of question and relation to mission.
        """
        mission = Mission.objects.create(name='Test Name', description='Some kind of description')
        open_ended_question = OpenEndedQuestion.objects.create(mission=mission, text='What kind of test should we create?')
        self.assertEqual(str(open_ended_question), open_ended_question.text)
        self.assertEqual(mission.question_set.all().count(), 1)

    def test_create_rating_questoin(self):
        """
        Test creation of question and relation to mission.
        """
        mission = Mission.objects.create(name='Test Name', description='Some kind of description')
        rating_question = RatingQuestion.objects.create(mission=mission, text='What kind of test should we create?')
        self.assertEqual(str(rating_question), rating_question.text)
        self.assertEqual(mission.question_set.all().count(), 1)


class AnswerModelTests(TestCase):
    def test_create_open_ended_answer(self):
        """
        Test creation of answer and relation to question.
        """
        user = User.objects.create(username='Tester')
        mission = Mission.objects.create(name='Test Name', description='Some kind of description')
        open_ended_question = OpenEndedQuestion.objects.create(mission=mission, text='What kind of test should we create?')
        open_ended_answer = OpenEndedAnswer.objects.create(question=open_ended_question, response='Let\'s create an open ended anser!', user=user)
        self.assertEqual(str(open_ended_answer), open_ended_answer.response)
        self.assertEqual(open_ended_question.openendedanswer_set.all().count(), 1)

    def test_rating_answer(self):
        """
        Test creation of answer and relation to question.
        """
        user = User.objects.create(username='Tester')
        mission = Mission.objects.create(name='Test Name', description='Some kind of description')
        rating_question = RatingQuestion.objects.create(mission=mission, text='What kind of test should we create?')
        rating_answer = RatingAnswer.objects.create(question=rating_question, response=8, user=user)
        self.assertEqual(rating_answer.response, 8)
        self.assertEqual(rating_question.ratinganswer_set.all().count(), 1)
