from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Couples
import random
# Create your views here.

def index(request):
    if request.method == "POST":
        username = request.POST.get('username')
        crushname = request.POST.get('crushname')
        score = random.randint(50,100)
        Couples.objects.create(user_name=username, crush_name= crushname, score=score)

        return redirect("display")
    return render(request, "crush/index.html")

def display(request):
    random_score = random.randint(50,100)
    return render(request, "crush/display.html", {"random_score":random_score})


def all_display(request):
    alldata = Couples.objects.all()
    return render(request, "crush/alldisplay.html", {"alldata":alldata})