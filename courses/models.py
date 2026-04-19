from django.db import models


class Course(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Lesson(models.Model):
    title = models.CharField(max_length=200)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Question(models.Model):
    text = models.CharField(max_length=300)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)

    def __str__(self):
        return self.text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)


class Submission(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    score = models.IntegerField(default=0)
