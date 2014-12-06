from django.db import models

# Create your models here.
class Survey(models.Model):
    title = models.CharField(max_length=300),

class Question(models.Model):
    question_text = models.CharField(max_length=900),
    survey = models.ForeignKey(Survey)

class Choice(models.Model):
    choice_text = models.CharField(max_length=900),
    question = models.ForeignKey(Question)

class SurveyAnswer(models.Model):
    orig_survey = models.ForeignKey(Survey)

class QuestionAnswer(models.Model):
    answer = models.ForeignKey(Choice)
    survey_answer = models.ForeignKey(SurveyAnswer)

