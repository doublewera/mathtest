from django.db import models

# Create your models here.


class Question(models.Model):
    question_text = models.CharField(max_length=16)
    right_answer = models.IntegerField()

    def __str__(self):
        return self.question_text + " = "


class Answer(models.Model):
    answer = models.IntegerField()

    def __str__(self):
        return str(self.answer)
