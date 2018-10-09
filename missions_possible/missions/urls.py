from django.urls import path
from django.conf.urls import url

from . import views


app_name = 'missions'
urlpatterns = [
    path('', views.MissionIndexView.as_view(), name='index'),
    path('add_mission/', views.MissionCreateView.as_view(), name='add_mission'),
    path('<int:pk>/', views.MissionDetailView.as_view(), name='mission_detail'),
    url(r'^(?P<mission_id>\d+)/add_question/$', views.OpenEndedQuestionCreateView.as_view(), name='add_question'),
]
