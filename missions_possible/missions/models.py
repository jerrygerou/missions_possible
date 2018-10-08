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


# Would ideally like to create a model for Question with 'type' as an attribute.
# Brings about complications for other attributes and form behavior.
# For now, just creating two separate model classes.
class OpenEndedQuestion(models.Model):
    """
    A question belongs to a mission and can be answered by a user.
    """
    mission = models.ForeignKey(Mission, on_delete=models.CASCADE)
    text = models.CharField(
        max_length=500,
        blank=False,
        default=''
    )

    def __str__(self):
        return self.text


class RatingQuestion(models.Model):
    """
    A rating question belongs to a mission and can be answered by a user.
    """
    mission = models.ForeignKey(Mission, on_delete=models.CASCADE)
    text = models.CharField(
        max_length=500,
        blank=False,
        default=''
    )

    def __str__(self):
        return self.text
