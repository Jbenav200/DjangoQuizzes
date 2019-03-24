from django.shortcuts import render


def home(request):
    return render(request, 'quiz/home.html')


def user_home(request):
    return render(request, 'quiz/user_home.html', {'title': 'Home'})


def report(request):
    return render(request, 'quiz/report.html', {'title': 'Report'})


def questions(request):
    return render(request, 'quiz/questions.html', {'title': 'Questions'})

# GET -> asks for stuff
# POST -> sends you stuff
# PUT -> very specific stuff or if you are a webdev from the 1990s
# HEAD -> headers
