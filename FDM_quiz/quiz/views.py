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
    score_list = UserScore.objects.order_by('score')
    context ={
        'score_list': score_list,
        'title': 'Ranking Table'
    }
    template = loader.get_template('quiz/ranking_table.html')
    return HttpResponse(template.render(context, request))


@login_required
def art(request):
    form = UserScoreArtForm(request.POST)
    context = {
        'form': form
    }

    if request.method == 'POST':
        form = UserScoreArtForm(request.POST)
    if form.is_valid():
        ml = request.POST['ml']
        vg = request.POST['vg']
        # user_score to be placed here
        if ml == "7" and vg == "10":
            username = request.user.username
            score = 20
            a = UserScore()
            a.username = username
            categories = Category.objects.filter(name='Art')
            for c in categories:
                a.category = c
            a.score = score
            a.save()
            return redirect('/results')
        elif ml == "7" and "10" not in vg:
            username = request.user.username
            score = 10
            a = UserScore()
            a.username = username
            categories = Category.objects.filter(name='Art')
            for c in categories:
                a.category = c
            a.score = score
            a.save()
            return redirect('/results')
        elif "7" not in ml and vg == "10":
            username = request.user.username
            score = 10
            a = UserScore()
            a.username = username
            categories = Category.objects.filter(name="Art")
            for c in categories:
                a.category = c
            a.score = score
            a.save()
            return redirect('/results')
        else:
            return redirect('/quizzes/art')
    return render(request, 'quiz/art.html', context)


@login_required
def history(request):
    form = UserScoreHistoryForm(request.POST)
    context = {
        'form': form,
    }

    if request.method == 'POST':
        form = UserScoreHistoryForm(request.POST)
        if form.is_valid():
            w2 = request.POST['w2']
            w1 = request.POST['w1']
            # user_score to be placed here
            if w2 == "1" and w1 == "22":
                    username = request.user.username
                    score = 20
                    a = UserScore()
                    a.username = username
                    categories = Category.objects.filter(name='History')
                    for c in categories:
                        a.category = c
                    a.score = score
                    a.save()
                    return redirect('/results')
            elif w1 == "22" and "1" not in w2:
                username = request.user.username
                score = 10
                a = UserScore()
                a.username = username
                categories = Category.objects.filter(name="History")
                for c in categories:
                    a.category = c
                a.score = score
                a.save()
                return redirect('/results')
            elif "22" not in w1 and w2 == "1":
                username = request.user.username
                score = 10
                a = UserScore()
                a.username = username
                categories = Category.objects.filter(name="History")
                for c in categories:
                    a.category = c
                a.score = score
                a.save()
                return redirect('/results')
            else:
                return redirect('/quizzes/history')
        else:
            return redirect('/quizzes/history')
    return render(request, 'quiz/history.html', context)


@login_required
def books(request):
    form = UserScoreBooksForm(request.POST)
    context = {
        'form': form,
    }

    if request.method == 'POST':
        form = UserScoreBooksForm(request.POST)
        if form.is_valid():
            hp = request.POST['hp']
            wp = request.POST['wp']
            if hp == "14" and wp == "18":
                    username = request.user.username
                    score = 20
                    a = UserScore()
                    a.username = username
                    categories = Category.objects.filter(name='Books')
                    for c in categories:
                        a.category = c
                    a.score = score
                    a.save()
                    return redirect('/results')
            elif hp == "14" and "18" not in wp:
                username = request.user.username
                score = 10
                a = UserScore()
                a.username = username
                categories = Category.objects.filter(name="Books")
                for c in categories:
                    a.category = c
                a.score = score
                a.save()
                return redirect('/results')
            elif "14" not in hp and wp == "18":
                username = request.user.username
                score = 10
                a = UserScore()
                a.username = username
                categories = Category.objects.filter(name="Books")
                for c in categories:
                    a.category = c
                a.score = score
                a.save()
                return redirect('/results')
            else:
                return redirect('/quizzes/books')
    return render(request, 'quiz/books.html', context)


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
