from django.db import models
from django.contrib.auth.models import User  # import table User


class Question(models.Model):
    question_text = models.CharField(max_length=16)
    right_answer = models.IntegerField()

    def __str__(self):
        return self.question_text + " = "


class Answer(models.Model):
    answer = models.IntegerField()
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        default=0)
    # user is now connected to db!
    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
        default=0)
    dt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s %i. Suggested by %s at %s" % (
            str(self.question),
            self.answer_int,
            self.author,
            self.dt.strftime("%Y-%m-%d %H:%M:%S")
            )


