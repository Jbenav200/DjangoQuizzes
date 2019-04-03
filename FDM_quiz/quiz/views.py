from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template import loader
from .models import *


def home(request):
    return render(request, 'quiz/home.html')


def about(request):
    return render(request, 'quiz/about.html', {'title': 'About'})


@login_required
def quizzes(request):
    questions_list = Question.objects.order_by('question_text')
    choices_list = Choice.objects.order_by('question')
    categories_list = Category.objects.order_by('name')
    template = loader.get_template('quiz/questions.html')
    context = {
        'questions_list': questions_list,
        'title': "Questions",
        'choices_list': choices_list,
        'categories_list': categories_list,

    }
    return HttpResponse(template.render(context, request))
    # return render(request, 'quiz/quizzes.html', {'title': 'Quizzes'})  (idk what you do with your returns but try work my one in as well)


@login_required
def results(request):
    category_list = Category.objects.order_by('name')
    user_list = User.objects.order_by('username')
    from FDM_quiz import users
    username = users.models.User.return_username()
    template = loader.get_template("quiz/reports.html")
    context = {
        'category_list': category_list,
        'user_list': user_list,
        'title': "Report",
        'username': username,
    }
    return HttpResponse(template.render(context, request))
    # return render(request, 'quiz/results.html', {'title': 'Results'}) (idk what you do with your returns but try work my one in as well)


@login_required
def ranking_table(request):
    return render(request, 'quiz/ranking_table.html', {'title': 'Ranking Table'})


# GET -> asks for stuff
# POST -> sends you stuff
# PUT -> very specific stuff or if you are a webdev from the 1990s
# HEAD -> headers
