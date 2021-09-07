import random
from datetime import datetime

from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse , JsonResponse, HttpResponseRedirect, Http404
from django.template import loader
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import *
from django.urls import reverse

def index(request):
    category = request.GET.get('category')
    context = {
        'category' : category,
    }
    return render(request,'index.html',category)

def about(request):
    return render(request,'about.html')

def aboutX(request):
    return render(request,'aboutX.html')

def hire(request):
    return render(request,'hire.html')

#views.py
def studyroom(request):
    studyrooms = Studyroom.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(studyrooms, 10)
    try:
        studyrooms = paginator.page(page)
    except PageNotAnInteger:
        studyrooms = paginator.page(1)
    except EmptyPage:
        studyrooms = paginator.page(paginator.num_pages)
    context = {
        'studyrooms': studyrooms
    }

    return render(request, 'studyroom.html',context)

def activity(request):
    ranks = Board.objects.order_by('created_date')
    boards = {'boards': Board.objects.all(),
              'ranks':ranks
              }
    return render(request,'activity.html',boards)

def post(request):
    if request.method == "POST":
        author = request.POST['author']
        title = request.POST['title']
        content = request.POST['content']
        password = request.POST['password']
        board = Board(author=author, title=title, content=content, password=password)
        board.save()
        return HttpResponseRedirect(reverse('activity'))
    else:
        return render(request, 'post.html')

def detail(request, id):
    try:
        board = Board.objects.get(pk=id)
        comments = Comment.objects.filter(board=id)
        print(comments)
    except Board.DoesNotExist:
        raise Http404("Does not exist!")
    return render(request, 'detail.html', {'board': board, 'comments':comments})

def update(request,id):
    boarding = Board.objects.get(id=id)
    if request.method == 'POST' :
        if request.POST['password'] == boarding.password:
            boarding.author = request.POST['author']
            boarding.title = request.POST['title']
            boarding.content = request.POST['content']
            boarding.password = request.POST['password']
            boarding.save();
            return redirect("activity")
        else :
            return redirect("fail")
    else :
        context = { 'boarding' : boarding}
    return render(request,'update.html',context)

def delete(request,id):
    board = Board.objects.get(id=id)
    if request.method == 'POST':
        if request.POST['password'] == board.password:
            board.delete()
            return redirect("activity")
        else:
            return redirect("fail")
    else:
        context = {'board': board}
    return render(request, 'delete.html', context)


def hire(request):
    hires=Company.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(hires, 10)
    try:
        hires = paginator.page(page)
    except PageNotAnInteger:
        hires = paginator.page(1)
    except EmptyPage:
        hires = paginator.page(paginator.num_pages)
    context = {
        'hires': hires
    }
    return render(request,'hire.html',context)

def fail(request):
    return render(request, 'fail.html')
'''
def comment(request,id):
    comments = Board.objects.filter(id=id)
    if request.method == "POST":
        author = request.POST['author']
        content = request.POST['content']
        comment = Comment(author=author, content=content)
        comment.save()
    return render(request,'comment.html',comments)
'''


def comment(request,id):
    comments = Comment.objects.filter(board = id)
    print(comments)
    if request.method == "POST":
        author = request.POST['author']
        content = request.POST['content']
        password = request.POST['password']
        board = Board.objects.get(id = id)
        comment = Comment(board=board, author=author, content=content, password=password)
        comment.save()
        return redirect("activity")
    context = {
            "comments" : comments,
            "id" : id
    }
    return render(request,'comment.html',context)


def comment_update(request,id):
    commenting = Comment.objects.get(id=id)
    if request.method=='POST':
        if request.POST['password'] == commenting.password:
            commenting.author = request.POST['author']
            commenting.content = request.POST['content']
            commenting.password = request.POST['password']
            commenting.save();
            return redirect("activity")
        else:
            return redirect("fail")
    else :
        context = {'commenting': commenting}
    return render(request,'comment_update.html',context)


def comment_delete(request,id):
    comment = Comment.objects.get(id=id)
    if request.method == 'POST':
        if request.POST['password'] == comment.password:
            comment.delete()
            return redirect("activity")
        else:
            return redirect("fail")
    else:
        context = {'comment': comment}
    return render(request,'comment_delete.html',context)


