from django.conf import settings
from django.db import models


class Mission(models.Model):
    """
    A mission is a collection of questions.
    """
    name = models.CharField(
        max_length=255,
        blank=False,
        default=''
    )
    description = models.TextField()

    def __str__(self):
        return self.name


class Question(models.Model):
    """
    Parent class for different kinds of questions.
    """
    mission = models.ForeignKey(Mission, on_delete=models.CASCADE)
    text = models.CharField(
        max_length=500,
        blank=False,
        default=''
    )

    def __str__(self):
        return self.text


class OpenEndedQuestion(Question):
    """
    A question belongs to a mission and can be answered by a user.
    """


class RatingQuestion(Question):
    """
    A rating question belongs to a mission and can be answered by a user.
    """
