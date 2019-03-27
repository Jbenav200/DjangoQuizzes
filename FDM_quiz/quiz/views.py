from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'quiz/home.html')


def about(request):
    return render(request, 'quiz/about.html', {'title': 'About'})


@login_required
def quizzes(request):
    return render(request, 'quiz/quizzes.html', {'title': 'Quizzes'})


@login_required
def results(request):
    return render(request, 'quiz/results.html', {'title': 'Results'})


@login_required
def ranking_table(request):
    return render(request, 'quiz/ranking_table.html', {'title': 'Ranking Table'})


# GET -> asks for stuff
# POST -> sends you stuff
# PUT -> very specific stuff or if you are a webdev from the 1990s
# HEAD -> headers
