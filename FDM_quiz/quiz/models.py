from django.db import models
from django.forms import ModelForm, forms
from django.template.backends import django

from .models import *


# Create your models here.
# Category model
class Category(models.Model):
    id = models.IntegerField(primary_key=1, auto_created=1)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.name


# Question model
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    correct_answer = models.CharField(max_length=200)
    published_date = models.DateTimeField('date published')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.question_text

    def return_category(self):
        return self.category


# Choice model
class Choice(models.Model):
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return self.choice_text

    def __question__(self):
        return self.question


# User model
class User(models.Model):
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.name, self.username


class UserScore(models.Model):
    id = models.IntegerField(primary_key=1, auto_created=1)
    username = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    score = models.IntegerField()

    def __str__(self):
        return self.username

    def __category__(self):
        return self.category

    def __score__(self):
        return self.score

