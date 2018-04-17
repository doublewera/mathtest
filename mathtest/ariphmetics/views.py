from django.shortcuts import get_object_or_404, get_list_or_404, render
from django.http import HttpResponse
from .models import Question, Answer
from django.contrib.auth.models import User
from random import sample
import django.contrib.staticfiles
from django.template import RequestContext
from django.shortcuts import render_to_response


h = '0,1,2,3,4,5,6,7,8,9,a,b,c,d,e,f'.split(',')

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

def db_print(request): 
    questions = Question.objects.order_by('id')
    # returns a list of Question class objects
    # questions = [Question(), Question() ........]
    quest_ans = {}
    for q in questions:
        quest_ans.update({q.question_text: q.right_answer})
    print(quest_ans)
    answers = Answer.objects.order_by('id')
    ans_by_u = {} 
    for i in answers:
        i = str(i)
        question = i[:i.index('=')].strip()
        answer = int(i[i.index('=') + 1: i.index('. ')].strip())        
        user = i[i.index('by ') + 3: i.index(' at ')].strip()
        date_time = i[i.index(' at ') + 4:].strip()
        right_answer = quest_ans[question]
        if ans_by_u.get(user):
            ans_by_u[user].append([
                
                question,
                answer,
                right_answer,
                date_time,
                ])
        else:
            ans_by_u.update({user: [[
                question,
                answer,
                right_answer,
                date_time,
                ]]})
    for user in ans_by_u.keys():
        for date in ans_by_u[user]:
            date.append(len(ans_by_u[user]))
    users = User.objects.order_by('id')
    context = {
        "user_answers": ans_by_u,
    }
    return render_to_response( "answers.html", context) 
   
    
