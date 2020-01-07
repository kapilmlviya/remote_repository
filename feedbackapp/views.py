from django.shortcuts import render
from feedbackapp.form import feedbackForm
from feedbackapp.models import feedbackData
from django.http.response import HttpResponse
import  datetime as dt
date1=dt.datetime.now()

def feedbackview(request):
    if request.method=="POST":
        fform=feedbackForm(request.POST)
        if fform.is_valid():
            name1=request.POST.get('name')
            rating1=request.POST.get('rating')
            feedback1=request.POST.get('feedback')

            data =feedbackData(
                name=name1,
                rating=rating1,
                date=date1,
                feedback=feedback1
            )
            data.save()
            fform=feedbackForm()
            feedback=feedbackData.objects.all()
            return render (request,'feedback.html',{'fform':fform ,'feedbacks':feedback})
        else:
            return  HttpResponse("user missed some values")
    else:
        fform = feedbackForm()
        feedback = feedbackData.objects.all()
        return  render(request,'feedback.html',{'fform':fform,'feedbacks':feedback})



# Create your views here.
