from django.shortcuts import render, redirect
from models import Survey, SurveyAnswer, QuestionAnswer, Choice, Question
from django.contrib.auth import authenticate, login

# Create your views here.
def index(request):
    ctx = {}
    return render(request, "main.html", ctx)

def survey_view(request, survey_id = None):
    try:
        survey = Survey.objects.get(id=survey_id)
        questions = survey.question_set.all()
        ctx = {'survey' : survey, 'questions' : questions}
    except:
        return render(request, "surveynotfound-error.html", {'sv_id' : survey_id})
    return render(request, "survey-take.html", ctx)

def load_survey(request):
    sv_to_load = request.POST['survey_view']
    return redirect('survey-detail', survey_id = sv_to_load)

def survey_fill(request):
    answer = SurveyAnswer()
    orig_survey = Survey.objects.get(id = request.POST['survey_id'])
    answer.orig_survey = orig_survey
    answer.save()
    questions = orig_survey.question_set.all()
    for question in questions:
        question_post = request.POST['question']
        QA = QuestionAnswer()
        QA.answer = Choice.objects.get(id = int(question_post))
        QA.survey_answer = answer
        QA.save()
    answer.save()
    return render(request, 'survey-complete.html', {})

def admin_login(request):
    admin_username = request.POST['username']
    admin_password = request.POST['password']
    user = authenticate(username = admin_username, password = admin_password)
    if user is not None:
        login(request, user)
        return redirect(('admin-panel'))
    return render(request, 'main.html', {'login': False})

def admin_panel(request):
    surveys = Survey.objects.all()
    ctx = {'surveys': surveys}
    return render(request, 'admin-panel.html', ctx)

def survey_delete(request):
    survey_deletion = request.POST['sv_delete']
    sv_del = Survey.objects.get(id=int(survey_deletion))
    sv_del.delete()
    return redirect('admin-panel')

def admin_answers(request, survey_id):
    survey = Survey.objects.get(id = survey_id)
    answers = survey.surveyanswer_set.all()
    ctx = {'answers' : answers, 'survey' : survey}
    return render(request, 'admin-survey-detail.html', ctx)

def survey_create_view(request):
    return render(request, 'survey-create.html', {})

def question_add_view(request):
    return render(request, 'question-add.html', {})

def choice_add_view(request):
    question = Question.objects.get(id=int(request.session['current_question']))
    return render(request, 'choice-add.html', {'question' : question})

def survey_create(request):
    newSurvey = Survey()
    newSurvey.title = request.POST['survey_title']
    newSurvey.save()
    request.session['current_survey'] = newSurvey.id
    return redirect('admin-question-add-view')

def question_add(request):
    survey_add = Survey.objects.get(id=int(request.session['current-survey']))
    new_question = Question()
    new_question.question_text = request.POST['question_text']
    survey_add.question_set.add(new_question)
    new_question.save()
    survey_add.save()
    request.session['current_question'] = new_question.id
    return redirect('admin-choice-add-view')

def choice_add(request):
    question = Question.objects.get(id =int(request.session['current_question']))
    newChoice = Choice()
    newChoice.choice_text = request.POST['choice_text']
    question.choice_set.add(newChoice)
    newChoice.save()
    question.save()
    return redirect('admin-choice-add-view')