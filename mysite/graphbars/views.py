from django.shortcuts import render
from . models import Department, Student, Teacher, Project

# Create your views here.
def index(response):
    cseStd= Department.objects.get(name="cse").student_set.count()
    eeeStd= Department.objects.get(name="eee").student_set.count()
    ceStd= Department.objects.get(name="ce").student_set.count()
    teStd= Department.objects.get(name="te").student_set.count()
    meStd= Department.objects.get(name="me").student_set.count()

    cseTeac= Department.objects.get(name="cse").teacher_set.count()
    eeeTeac= Department.objects.get(name="eee").teacher_set.count()
    ceTeac= Department.objects.get(name="ce").teacher_set.count()
    teTeac= Department.objects.get(name="te").teacher_set.count()
    meTeac= Department.objects.get(name="me").teacher_set.count()

    cseProj= Department.objects.get(name="cse").project_set.count()
    eeeProj= Department.objects.get(name="eee").project_set.count()
    ceProj= Department.objects.get(name="ce").project_set.count()
    teProj= Department.objects.get(name="te").project_set.count()
    meProj= Department.objects.get(name="me").project_set.count()
    
    # student = {
    #     "cse": cse.student_set.count(),
    #     "eee": eee.student_set.count(),
    #     "ce": ce.student_set.count(),
    #     "te": te.student_set.count(),
    #     "me": me.student_set.count()
    # }
    return render(response, 'graphbars/graph.html', {
        "cseStd":cseStd, 
        "eeeStd":eeeStd,
        "ceStd":ceStd,
        "teStd":teStd,
        "meStd":meStd,
        "cseTeac":cseTeac,
        "eeeTeac":eeeTeac,
        "ceTeac":ceTeac,
        "teTeac":teTeac,
        "meTeac":meTeac,
        "cseProj":cseProj,
        "eeeProj":eeeProj,
        "ceProj":ceProj,
        "teProj":teProj,
        "meProj":meProj
    })
