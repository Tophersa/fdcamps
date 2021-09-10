from django.db import models

class Motivation(models.Model):
    motiveType = models.CharField(max_length=200, null=True, blank=True)
    author = models.CharField(max_length=200, null=True, blank=True)
    imagelink = models.CharField(max_length=10000, null=True, blank=True)
    lifetime = models.CharField(max_length=200, null=True, blank=True)
    quote = models.TextField(max_length=1000, null=True, blank=True)
    def __str__(self):
        return self.motiveType


# class Grade(models.Model):
#     grade = models.CharField(max_length=200)
#     def __str__(self):
#         return self.grade

class Subject(models.Model):
    # grade = models.ForeignKey(Grade, on_delete=models.CASCADE)
    grade = models.CharField(max_length=200)
    subject = models.CharField(max_length=200, null=True)
    #year = models.CharField(max_length=200, null=True)
    #questionPaper = models.CharField(max_length=200, null=True)
    def __str__(self):
        return self.subject + " " + self.grade

class Year(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    retypeSubject = models.CharField(max_length=200, null=True)
    year = models.CharField(max_length=200)
    def __str__(self):
        return self.year +" " + self.retypeSubject

class QuestionPaper(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, null=True)
    retypeSubject = models.CharField(max_length=200, null=True)
    grade = models.CharField(max_length=200, null=True)
    year = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    link = models.CharField(max_length=10000, null=True)
    def __str__(self):
        return self.retypeSubject + " " + self.name + " " + self.year
