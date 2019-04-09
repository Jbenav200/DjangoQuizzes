from .models import *
from django import forms


class UserScoreForm(ModelForm):
    class Meta:
        model = UserScore
        fields = ['username', 'category', 'score']


class UserScoreArtForm(UserScoreForm):
    question_list = Question.objects.filter(category=2)
    choice_list = Choice.objects.none()

    for q in question_list:
        if q.question_text == 'When did Van Gough Die?':
            vg = forms.ModelMultipleChoiceField(queryset=Choice.objects.filter(question_id=q.id).order_by('choice_text'), label=q)

        if q.question_text == 'When was the Mona Lisa painted?':
            ml = forms.ModelMultipleChoiceField(queryset=Choice.objects.filter(question_id=q.id).order_by('choice_text'), label=q)

    class Meta(UserScoreForm.Meta):
        fields = ['vg', 'ml']


class UserScoreHistoryForm(UserScoreForm):
    question_list = Question.objects.filter(category=1)
    choice_list = Choice.objects.none()
    for q in question_list:
        if q.question_text == 'When did World War II end?':
            w2 = forms.ModelMultipleChoiceField(queryset=Choice.objects.filter(question_id=q.id).order_by('choice_text'), label=q)
        if q.question_text == 'When did World War I end?':
            w1 = forms.ModelMultipleChoiceField(queryset=Choice.objects.filter(question_id=q.id).order_by('choice_text'), label=q)

    class Meta(UserScoreForm.Meta):
        fields = ['w2', 'w1']


class UserScoreBooksForm(UserScoreForm):
    question_list = Question.objects.filter(category=3)
    choice_list = Choice.objects.none()
    for q in question_list:
        if q.question_text == 'Who wrote the Harry Potter series?':
            hp = forms.ModelMultipleChoiceField(queryset=Choice.objects.filter(question_id=q.id).order_by('choice_text'), label=q)
        if q.question_text == 'Who wrote the original Winnie The Pooh series?':
            wp = forms.ModelMultipleChoiceField(queryset=Choice.objects.filter(question_id=q.id).order_by('choice_text'), label=q)

    class Meta(UserScoreForm.Meta):
        fields = ['hp', 'wp']
