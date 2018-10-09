from django.conf import settings
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


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
    type = models.CharField(
        max_length=25,
        default='open_ended'
    )


class RatingQuestion(Question):
    """
    A rating question belongs to a mission and can be answered by a user.
    """
    type = models.CharField(
        max_length=25,
        default='rating'
    )


# Not sure at this point if I can do a parent class for Answers
# - what model would the foreign key refer to?
# - the response fields are different field types
# So creating separate model classes for each kind of answer for now
class OpenEndedAnswer(models.Model):
    """
    Answer relating to OpenEndedQuestion(s)
    """
    question = models.ForeignKey(OpenEndedQuestion, on_delete=models.CASCADE)
    response = models.CharField(
        max_length=500,
        default = ''
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, default='')

    def __str__(self):
        return self.response


class RatingAnswer(models.Model):
    """
    Answer relating to RatingQuestion(s)
    """
    question = models.ForeignKey(RatingQuestion, on_delete=models.CASCADE)
    response = models.IntegerField(
        default=0,
        validators=[
            MaxValueValidator(10),
            MinValueValidator(0)
        ]
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, default='')

    def __int__(self):
        return self.response
