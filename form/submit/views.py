from django.shortcuts import render
from submit.models import Submit


def save(request):
    if request.method == "POST":
        username = request.POST.get('username')
        emailid = request.POST.get('email_id')
        data = Submit(Uname=username, email=emailid)
        data.save()
    return render(request, "index.html")
