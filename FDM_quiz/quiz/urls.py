from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='quiz-home'),
    path('about/', views.about, name='quiz-about'),
    path('quizzes/', views.quizzes, name='quiz-quizzes'),
    path('results/', views.results, name='quiz-results'),
    path('ranking_table/', views.ranking_table, name='quiz-ranking_table'),
    path('quizzes/art', views.art, name='art'),
    path('quizzes/history', views.history, name='History'),
    path('quizzes/books', views.books, name='Books'),
]
