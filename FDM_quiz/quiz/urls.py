from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='quiz-home'),
    path('about/', views.about, name='quiz-about'),
    path('quizzes/', views.quizzes, name='quiz-quizzes'),
    path('results/', views.results, name='quiz-results'),
    path('ranking_table/', views.ranking_table, name='quiz-ranking_table'),

]
