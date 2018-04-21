from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import Question, Answer
from django.contrib.auth.models import User
# from django.contrib.auth import authenticate, login
from random import sample, randint


def index(request, question_count=1):
    questions = Question.objects.order_by('id')
    # user = authenticate(
    #    request,
    #    username=request.POST["username"],
    #    password=request.POST["password"])
    # todo: check unauthorized!
    # reimplementing __missing__ is better :)
    if question_count == 0:
        if "question_count" in request.POST:
            question_count = int(request.POST["question_count"])
        else:
            question_count = randint(1, len(questions))
    theuser = "admin"
    if "username" in request.POST:
        theuser = request.POST["username"]
    context = {
        "debug": 'user: %s' % (
            theuser,
            # request.POST["next"]
            ),
        "user": theuser,
        # I'd like to write context["user"] = request.POST["username"]
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
        if not qid.startswith("qid"):
            continue
        q = get_object_or_404(Question, pk=int(qid[len("qid"):]))
        answer = Answer.objects.create(
            answer=request.POST[qid],
            author=author,
            question=q
            )
        answer.save()
    return HttpResponse("Your solutions have been recorded to DB.")

def answer_list(request):
    #answers = Answers.objects.filter(author="wera")
    context = {"listelems": Answer.objects.all()}
    return render(request, "list.html", context)

def user_list(request):
    users = User.objects.order_by('id')
    context = {
        "listelems": users,
    }
    return render(request, "list.html", context)
