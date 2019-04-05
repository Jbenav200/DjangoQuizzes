from django import forms
from .models import *


class ArtQuestionsForm(forms.Form):
    question_list = Question.objects.filter(category=2)
    choice_list = Choice.objects.none()

    for q in question_list:
        question = forms.ModelMultipleChoiceField(queryset=Choice.objects.filter(question_id=q.id))

    def __init__(self, question):
            super(ArtQuestionsForm, self).__init__()
            question_list = Question.objects.filter(category=2)
            for q in question_list:
                self.fields['question'].label = q
                self.fields['question'].queryset = Choice.objects.filter(question_id=q.id)
