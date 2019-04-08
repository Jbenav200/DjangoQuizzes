from django import forms
from .models import *


class ArtQuestionsForm(forms.Form):
    question_list = Question.objects.filter(category=2)
    choice_list = Choice.objects.none()

    for q in question_list:
        quest = forms.ModelMultipleChoiceField(queryset=Choice.objects.filter(question_id=q.id), label=q)

    def __init__(self, quest):
            super(ArtQuestionsForm, self).__init__()
