from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from django.http import HttpResponse
from django.shortcuts import render

from jobsapp import forms
from jobsapp.models import Hydjobsinfo,Delhijobsinfo,Punejobsinfo,Noidajobsinfo

def home(request):
    return render(request,'jobsapp/home.html')

def hydjobs(request):
    hydjobs_list = Hydjobsinfo.objects.all()
    paginator = Paginator(hydjobs_list,3)
    page_number= request.GET.get('page')
    try:
        hydjobs_list=paginator.page(page_number)
    except PageNotAnInteger:
        hydjobs_list=paginator.page(1)
    except EmptyPage:
        hydjobs_list=paginator.page(paginator.num_pages)
    return render(request,'jobsapp/hydjobs.html', {'data1':hydjobs_list})

def delhijobs(request):
    delhijobs_list = Delhijobsinfo.objects.all()
    return render(request,'jobsapp/delhijobs.html', {'data2':delhijobs_list})

def Punejobs(request):
    punejobs_list = Punejobsinfo.objects.all()
    paginator = Paginator(punejobs_list, 3)
    page_number = request.GET.get('page')
    try:
        punejobs_list = paginator.page(page_number)
    except PageNotAnInteger:
        punejobs_list = paginator.page(1)
    except EmptyPage:
        punejobs_list = paginator.page(paginator.num_pages)
    return render(request,'jobsapp/punejobs.html', {'data3':punejobs_list})

def Noidajobs(request):
    noidajobs_list = Noidajobsinfo.objects.all()

    return render(request,'jobsapp/noidajobs.html', {'data4':noidajobs_list})


def Stud(request):
    form = forms.Student()
    return render(request,'jobsapp/forms.html', {'form':form})


def send(request):
    return HttpResponse('data send')