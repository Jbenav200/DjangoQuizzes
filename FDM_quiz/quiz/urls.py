from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='quiz-home'),
    path('user_home/', views.user_home, name='quiz-user_home'),
    path('report/', views.report, name='quiz-report'),
    path('questions/', views.questions, name='quiz-questions'),
]
