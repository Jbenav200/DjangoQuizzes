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
    categories_list = Category.objects.order_by('name')
    template = loader.get_template('quiz/quizzes.html')
    context = {
        'title': "Quizzes",
        'categories_list': categories_list,

    }
    return HttpResponse(template.render(context, request))
    # return render(request, 'quiz/quizzes.html', {'title': 'Quizzes'})  (idk what you do with your returns but try work my one in as well)


@login_required
def results(request):
    category_list = Category.objects.order_by('name')
    user_list = User.objects.order_by('username')
    username = "test"
    template = loader.get_template("quiz/results.html")
    context = {
        'category_list': category_list,
        'user_list': user_list,
        'title': "Results",
        'username': username,
    }
    return HttpResponse(template.render(context, request))
    # return render(request, 'quiz/results.html', {'title': 'Results'}) (idk what you do with your returns but try work my one in as well)


@login_required
def ranking_table(request):
    return render(request, 'quiz/ranking_table.html', {'title': 'Ranking Table'})


@login_required
def art(request):
    questions_list = Question.objects.filter(category=2)
    choice_list = Choice.objects.order_by('question')
    template = loader.get_template('quiz/art.html')
    context = {
        'title': "Art",
        'questions_list': questions_list,
        'choice_list': choice_list,
    }
    return HttpResponse(template.render(context, request))


@login_required
def history(request):
    questions_list = Question.objects.filter(category=1)
    choice_list = Choice.objects.order_by('question')
    context = {
        'title': 'History',
        'questions_list': questions_list,
        'choice_list': choice_list,
    }
    template = loader.get_template('quiz/history.html')
    return HttpResponse(template.render(context, request))


@login_required
def books(request):
    questions_list = Question.objects.filter(category=3)
    choice_list = Choice.objects.order_by('question')
    context = {
        'title': 'Books',
        'questions_list': questions_list,
        'choice_list': choice_list,
    }
    template = loader.get_template('quiz/books.html')
    return HttpResponse(template.render(context, request))

# GET -> asks for stuff
# POST -> sends you stuff
# PUT -> very specific stuff or if you are a webdev from the 1990s
# HEAD -> headers
