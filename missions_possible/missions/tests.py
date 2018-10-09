from django.test import TestCase

from .models import Mission, OpenEndedQuestion, RatingQuestion, OpenEndedAnswer, RatingAnswer


class MissionModelTest(TestCase):

    def create_mission(self, name='Test Name', description='Some kind of description'):
        mission = Mission.objects.create(name=name, description=description)
        self.assertEqual(str(mission), mission.name)
