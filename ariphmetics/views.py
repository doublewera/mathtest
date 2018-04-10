from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import Question, Answer
from django.contrib.auth.models import User
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
    author = get_object_or_404(User, username=request.POST["user"])
    token = request.POST["csrfmiddlewaretoken"]
    for qid in request.POST:
        if qid[0] != 'a':
            continue
        q = get_object_or_404(Question, pk=int(qid[1:]))
        answer = Answer.objects.create(
            answer=request.POST[qid],
            author=author,
            question=q
            )
        answer.save()
    return HttpResponse("Your answer was %s " % str(request.POST.keys()))


def user_list(request):
    return HttpResponse("<h2>here will be a user list</h2>")
