

# Create your views here.

import email
from django.shortcuts import render,redirect
from .models import User
import pickle
from django.http import HttpResponse
import joblib
from .models import Marks
from .models import Contact
# Create your views here.
# import joblib

def about(request):
  return render (request,"about.html")

def quiz(request):
    return render(request,"quiz.html")
def final1(request):
    return render(request,"final1.html")
def final(request):
    return render(request,"final.html")
def final2(request):
        return render(request,"final2.html")
def final3(request):
    return render(request,"final3.html")

def final1(request):
    return render(request,"final.html")
def Ebooks(request):
    return render(request,"Ebooks.Html")

def test(request):
    return render(request,"test.html")
def contact(request):
    return render(request,"contact.html")

def contact(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        contact=Contact(name=name,email=email,phone=phone)
        contact.save()
        #messages.success(request, 'Your msg has been send')
    return render(request,'contact.html')


def login(request):
    to = request.GET.get('to')
    if(request.method=="POST"):
        name = request.POST.get('user-name')
        password = request.POST.get('password')
        # try:
        user = User.objects.get(name=name,password=password)
        request.session['id'] = user.id
        request.session['email'] = user.email
        request.session['username'] = user.name

        if to:
             return redirect(to)
        return redirect('/')

        # except:
        #     return render(request,'login.html',{'name':name,'password':password,'error':'please fill correct id and password', 'to':to if to else ""})
    else:
        return render(request,'login.html', {'to':to if to else ""})



def signup(request):
    to = request.GET.get('to')
    if(request.method=="POST"):
        name = request.POST.get('user-name')
        password = request.POST.get('password')
        email = request.POST.get('email')
        if name=="" or password=="" or email=="":
            return render(request,'sign.html',{'name':name,'password':password,'email':email,'error':'Please fill all the details.', 'to':to if to else ""})
        try:
            user = User.objects.get(name=name)
            return render(request,'sign.html',{'name':name,'password':password,'email':email,'error':'User name already exists.', 'to':to if to else ""})
        except:
            pass
        try:
            user = User.objects.get(email=email)
            return render(request,'sign.html',{'name':name,'password':password,'email':email,'error':'Email already exists.', 'to':to if to else ""})
        except:
            pass
        user = User.objects.create(name=name,email=email,password=password)
        user.save()
        return redirect('/user/login?to='+(to if to else ""))
    else:
        return render(request,'sign.html', {'to':to if to else ""})




def home(request):
    return render(request,'home.html')


import joblib
def homepage(request):
    return render(request,'homepage.html')


def result(request):
    print("ok")
    cls=joblib.load("Stream_predictor_model.pkl")
    print("yup")
    lis=[]
    lis.append(request.GET['Maths'])
    lis.append(request.GET['English'])
    lis.append(request.GET['SocialScience'])
    lis.append(request.GET['Hindi'])
    lis.append(request.GET['Science'])
    lis.append(request.GET['Computers(optional)'])
    print(lis)
    ans=cls.predict([lis])

    return render(request,"result.html",{'ans':ans})

# def result(request):
#     cls=joblib.load("Stream_predictor_model.pkl")
#
#     lis=[]
#     lis.append(request.GET['Maths'])
#     lis.append(request.GET['English'])
#     lis.append(request.GET['SocialScience'])
#     lis.append(request.GET['Hindi'])
#     lis.append(request.GET['Science'])
#     lis.append(request.GET['Computers(optional)'])
#     print(lis)
#     ans=cls.predict([lis])
#
#     return render(request,"result.html",{'ans':ans})

def result1(request):
    cls=joblib.load("Student_mark_predictor_model.pkl")
    ans = "ok"
    if request.method == 'GET':
        lis=[]
        var=int(request.GET['Study_hour'])
        lis.append(var)
        print(lis)
        ans=cls.predict([lis])


    return render(request,"ans.html",{'ans':ans})
#
# def ml(request):
#     if request.method=="POST":
#         sports=int(request.POST.get('sports'))
#         artscraft=int(request.POST.get('artscraft'))
#         singing=int(request.POST.get('singing'))
#         acting=int(request.POST.get('acting'))
#         readingbooks=int(request.POST.get('readingbooks'))
#         dancing=int(request.POST.get('dancing'))
#         other=int(request.POST.get('other'))
#         marks=Marks(sports=sports,artscraft=artscraft,singing=singing,acting=acting,readingbooks=readingbooks,dancing=dancing,other=other)
#         marks.save()
#         L={ 'sports' : sports, 'artscraft':artscraft,'singing':singing,'acting':acting,'readingbooks':readingbooks,'dancing':dancing,'other':other}
#         tempList=[]
#         for ite in L:
# 	           if L[ite]>=6:
# 		            tempList.append(ite)
#         return render(request,"task.html",{"tempList":tempList})
#
#
#
#     return render(request,"task.html")

from django.http import HttpResponse
from django.shortcuts import render
from sklearn.preprocessing import Normalizer
import joblib
import pandas as pd
import numpy as np

def ml(request):
    if request.method=="POST":
        sports=int(request.POST.get('sports'))
        artscraft=int(request.POST.get('artscraft'))
        singing=int(request.POST.get('singing'))
        acting=int(request.POST.get('acting'))
        readingbooks=int(request.POST.get('readingbooks'))
        dancing=int(request.POST.get('dancing'))
        other=int(request.POST.get('other'))
        marks=Marks(sports=sports,artscraft=artscraft,singing=singing,acting=acting,readingbooks=readingbooks,dancing=dancing,other=other)
        marks.save()
        L={ 'sports' : sports, 'artscraft':artscraft,'singing':singing,'acting':acting,'readingbooks':readingbooks,'dancing':dancing,'other':other}
        tempList=[]
        for ite in L:
	           if L[ite]>=6:
		            tempList.append(ite)
        return render(request,"task.html",{"tempList":tempList})



    return render(request,"task.html")


def predict(request):
    form = request.POST or None
    print(request.method)
    criteria = {}
    if form:
        PercentageAlgorithms=int(request.POST.get('input1'))
        PercentagePREDICTION=int(request.POST.get('input2'))
        PercentagePrograming=int(request.POST.get('input3'))
        PercentageSoftware=int(request.POST.get('input4'))
        PercentageNetworks=int(request.POST.get('input5'))
        PercentageElectornics=int(request.POST.get('input6'))
        PercentagComputer=int(request.POST.get('input7'))
        PercentageMathmatics=int(request.POST.get('input8'))
        PercentagCommunication=int(request.POST.get('input9'))
        PercentageOperating=int(request.POST.get('input10'))
        HoursWorking=int(request.POST.get('input11'))
        Logicalquotient=int(request.POST.get('input12'))
        Hackathonsattended=int(request.POST.get('input13'))
        Codingskills=int(request.POST.get('input14'))
        Selflearningcapability=int(request.POST.get('input15'))
        Canworklong=int(request.POST.get('input16'))
        Olympiads=int(request.POST.get('input17'))
        Readingwritingskills=int(request.POST.get('input18'))
        ManagementTechnical=int(request.POST.get('input19'))
        HardSmartworker=int(request.POST.get('input20'))
        Workedteams=int(request.POST.get('input21'))
        criteria={"PercentageAlgorithms":PercentageAlgorithms,"PercentagePREDICTION":PercentagePREDICTION,"PercentagePrograming":PercentagePrograming,"PercentageSoftware":PercentageSoftware,"PercentageNetworks":PercentageNetworks,"PercentageElectornics":PercentageElectornics,"PercentagComputer":PercentagComputer,"PercentageMathmatics":PercentageMathmatics,"PercentagCommunication":PercentagCommunication,"PercentageOperating":PercentageOperating,"HoursWorking":HoursWorking}
        input = dict()
        li = []
        columns = ['Acedamic percentage in Operating Systems', 'percentage in Algorithms',
                   'Percentage in Programming Concepts',
                   'Percentage in Software Engineering', 'Percentage in Computer Networks',
                   'Percentage in Electronics Subjects',
                   'Percentage in Computer Architecture', 'Percentage in Mathematics',
                   'Percentage in Communication skills', 'Hours working per day',
                   'Logical quotient rating', 'hackathons', 'coding skills rating',
                   'public speaking points', 'can work long time before system?',
                   'self-learning capability?', 'Extra-courses did', 'olympiads',
                   'reading and writing skills', 'Management or Technical', 'hard/smart worker',
                   'worked in teams ever?']
        for i in range(len(request.POST) - 1):
            li.append(int(request.POST['input' + str(i)]))
        normalized_data1 = Normalizer().fit_transform([li[:14]])
        normalized_data2 = Normalizer().fit_transform([li[14:]])
        normalized_data = np.append(normalized_data1, normalized_data2, axis=1)
        for i, j in zip(range(len(request.POST) - 1), columns):
            input[j] = normalized_data[0][i]
        df = pd.DataFrame(input, index=[0])
        model = joblib.load('static/svm.pkl')
        labelencoder = joblib.load('static/label.pkl')
        results = model.predict(df)
        prediction = labelencoder.inverse_transform(results)
        criteria['prediction'] = prediction[0]
    return render(request, 'index-creative.html', criteria)
