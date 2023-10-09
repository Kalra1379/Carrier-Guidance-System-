from django.http import HttpResponse
from django.shortcuts import render

import joblib
def homepage(request):
    return render(request,'home.html')
def result(request):
    cls=joblib.load("Stream_predictor_model.pkl")

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
