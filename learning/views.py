from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import Grade,Subject, Year, QuestionPaper,Motivation

def index(request):
    gradeList = Grade.objects.all()
    subjectList = Subject.objects.all()
    yearList = Year.objects.all()
    qpList = QuestionPaper.objects.all()
    motivation = Motivation.objects.all()
    context = {
        'gradeList': gradeList,
        'subjectList': subjectList,
        'yearList': yearList,
        'qpList': qpList,
        'motivation': motivation,
    }
    return render(request, 'learning/index.html', context)
