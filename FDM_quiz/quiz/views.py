from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template import loader
from .models import *
from .forms import *


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
def ranking_table(request):
    return render(request, 'quiz/ranking_table.html', {'title': 'Ranking Table'})


@login_required
def art(request):
    questions_list = Question.objects.filter(category=2)
    choice_list = Choice.objects.all()
    template = loader.get_template('quiz/art.html')
    form = ArtQuestionsForm(questions_list)
    category = 'Art'
    context = {
        'questions_list': questions_list,
        'choices_list': choice_list,
        'form': form
    }
    if request.method == 'POST':
        form = ArtQuestionsForm(request.POST)
        if form.is_valid():
            ml = form.cleaned_data.get('ml')
            vg = form.cleaned_data.get('vg')
            # user_score to be placed here
            if ml == 7 and vg == 10:
                username = User.objects.filter(user__username=request.user.username)
                user_score = UserScore()
                user_score.username = username
                user_score.category = category
                user_score.score += 20
                user_score.save()
                return redirect('results')
            else:
                return redirect('home')
        return HttpResponse(template.render(context, request))
    return HttpResponse(template.render(context, request))


@login_required
def history(request):
    questions_list = Question.objects.filter(category=1)
    choices_list = Choice.objects.all()
    context = {
        'title': 'History',
        'questions_list': questions_list,
        'choices_list': choices_list,
    }
    template = loader.get_template('quiz/history.html')
    return HttpResponse(template.render(context, request))


@login_required
def books(request):
    questions_list = Question.objects.filter(category=3)
    choice_list = Choice.objects.all()
    context = {
        'title': 'Books',
        'questions_list': questions_list,
        'choices_list': choice_list,
    }
    template = loader.get_template('quiz/books.html')
    return HttpResponse(template.render(context, request))


@login_required
def results(request):
    score = UserScore.objects.all()
    context = {
        'score_list': score

    }
    template = loader.get_template('quiz/results.html')
    return HttpResponse(template.render(context, request))

# GET -> asks for stuff
# POST -> sends you stuff
# PUT -> very specific stuff or if you are a webdev from the 1990s
# HEAD -> headers
