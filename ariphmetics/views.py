from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import Question, Answer
from random import sample


def index(request, question_count=1):
    questions = Question.objects.order_by('id')
    context = {
        "debug": 'user: %s, pass: %s, next: %s' % (
            request.POST["username"],
            request.POST["password"],
            request.POST["next"]
            ),
        "user": request.POST["username"],
        "questions": sample(set(questions), question_count),
        "question_count": question_count,
        "suffix": "s" * (question_count > 1)
    }
    # return HttpResponse(template.render(context, request))
    return render(request, "index.html", context)


def solve(request):
    # user_answer = get_object_or_404(Answer)
    # return HttpResponse("Accepted %s" %
    # user_answer.choice_set.get(pk=request.POST['Choice']))
    # for key in .......
    result = ""
    for key in request.POST.keys():
        result += "%s : %s<br />" % (key, request.POST[key])
    return HttpResponse("Your answer was %s " % result)

