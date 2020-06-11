from django.shortcuts import render,redirect
# Create your views here.s
from . models import Course
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import pyforest
from sklearn.linear_model import LogisticRegression
from django.utils import timezone
import pickle
def page2(request):
    if request.method=="POST":
        a=request.POST['title']
        b=int(request.POST['age'])
        c1=request.POST['sex']
        if(c1=="Male"):
            val=1
        else:
            val=0
        d=float(request.POST['cigsperday'])
        e=float(request.POST['BPmeds'])
        f=int(request.POST['stroke'])
        g=int(request.POST['hyp'])
        h=int(request.POST['diabetes'])
        i=float(request.POST['sisBP'])
        j=float(request.POST['diaBP'])
        k=float(request.POST['BMI'])
        l=int(request.POST['heartrate'])
        c=Course()
        c.title=a
        c.age=b
        c.sex=val
        c.cigsperday=d
        c.BMmeds=e
        c.stroke=f
        c.hyp=g
        c.diabetes=h
        c.sisBP=i
        c.diaBP=j
        c.BMI=k
        c.heartrate=l
        test=[[b,val,d,0.0,g,h,i,j,k,l]]
        sca=StandardScaler()
        res=sca.fit_transform(test)
        model=pickle.load(open("C:/Users/tejak/Documents/heart_detection/detection/disease_predict/detect.pkl",'rb'))
        y_pred=model.predict(res)
        c.save()
        if(y_pred[0]==0):
            return render(request,'disease_predict/result.html',{'value':y_pred[0]})
        else:
            return render(request,'disease_predict/result2.html',{'value':y_pred[0]})
    else:
        return render(request,'disease_predict/home.html')
