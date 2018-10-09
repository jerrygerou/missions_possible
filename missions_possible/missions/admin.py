from django.contrib import admin

from .models import OpenEndedQuestion, OpenEndedAnswer, RatingQuestion, RatingAnswer

admin.site.register(OpenEndedQuestion)
admin.site.register(OpenEndedAnswer)
admin.site.register(RatingQuestion)
admin.site.register(RatingAnswer)
