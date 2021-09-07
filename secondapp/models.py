from django.db import models
from django.conf import settings


class Studyroom(models.Model):
    studynum=models.IntegerField(primary_key=True)
    studytitle=models.TextField()
    studycontent=models.TextField()
    studywriter=models.CharField(max_length=10)
    studylink=models.CharField(max_length=100)


    def __str__(self):
        return str(self.studynum)+","+self.studytitle+","+self.studycontent+","+self.studywriter+","+self.studylink


class Board(models.Model):
    author = models.CharField(max_length=10, null=False)
    title = models.CharField(max_length=100, null=False)
    content = models.TextField(null=False)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    password = models.CharField(max_length=10,null=True, default="None")

    def __str__(self):
        return self.author + ":" + self.title + ":" + self.content + ":" +str (self.created_date) + str(self.modified_date) + str(self.password)


class Company(models.Model):
    companyid=models.IntegerField(primary_key=True)
    companyname=models.CharField(max_length=50)
    companyjob=models.CharField(max_length=50)
    companydetail=models.CharField(max_length=50)
    companywork=models.CharField(max_length=50)
    companylocation=models.CharField(max_length=50)
    companydeadline=models.CharField(max_length=50)
    companyregister=models.CharField(max_length=50)


    def __str__(self):
        return str(self.companyid)+","+\
               self.companyname+","+self.companyjob+","+self.companydetail+","+self.companywork+","+\
                +self.companylocation+","+self.companydeadline+","+self.companyregister


class Comment(models.Model):
    board = models.ForeignKey(Board, on_delete=models.CASCADE, null=True)
    author = models.CharField(max_length=10, null=False)
    content = models.TextField(null=False)
    date= models.DateTimeField(auto_now_add=True)
    password = models.CharField(max_length=10, null=True, default="None")