from django.shortcuts import render
import datetime
# Create your views here.
def index(request):
    now = datetime.datetime.now()
    return render(request, "ALLSAINTSDAY/index.html", {
        "ALLSAINTSDAY": now.month ==11 and now.day ==1
    })