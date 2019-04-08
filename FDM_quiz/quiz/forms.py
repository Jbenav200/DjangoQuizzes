from django import forms
from .models import *


class ArtQuestionsForm(forms.Form):
    question_list = Question.objects.filter(category=2)
    choice_list = Choice.objects.none()

    for q in question_list:
        if q.question_text == 'When did Van Gough Die?' :
            vg = forms.ModelMultipleChoiceField(queryset=Choice.objects.filter(question_id=q.id), label=q)

        if q.question_text == 'When was the Mona Lisa painted?':
            ml = forms.ModelMultipleChoiceField(queryset=Choice.objects.filter(question_id=q.id), label=q)

    def __init__(self, question_list):
            super(ArtQuestionsForm, self).__init__()

            for q in question_list:
                if q == 'When did Van Gough Die?':
                    vg = forms.ModelMultipleChoiceField(queryset=Choice.objects.filter(question_id=q.id), label=q)
                if q == 'When was the Mona Lisa painted?':
                    ml = forms.ModelMultipleChoiceField(queryset=Choice.objects.filter(question_id=q.id), label=q)
