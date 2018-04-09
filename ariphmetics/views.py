from django.shortcuts import get_object_or_404, render
from django.template import loader
from django.http import HttpResponse
from .models import Question, Answer


def index(request, question_count=1):
    questions = Question.objects.order_by('id')
    # qlist_html = "\n".join(map(
    #    lambda q : "<li>%s</li>" % q,
    #    questions
    # ))

    # return HttpResponse("<h1>Try to solve %i example%s:</h1><ul>%s</ul>" % (
    #    question_count, "s" * (question_count > 1), qlist_html
    #    ))

    # template = loader.get_template("index.html")
    context = {
        "debug" : '%s' % question_count + str(len(questions)),
        "questions": questions[:question_count],
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
    return HttpResponse("Your answer was %s " % str(request.POST.keys()))
