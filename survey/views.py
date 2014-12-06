from django.shortcuts import render, redirect
from models import Survey, Question

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