from django.shortcuts import render, redirect
from app1.models import Login


def home(request):
    return render(request, "app1/home.html")

def reg(request):
    return render(request, "app1/reg.html")

def signup(request):
    print('signing up')
    if request.method == "POST":
        print('signing up if block')
        tfirst = request.POST.get('first')
        tmiddle = request.POST.get('middle', '')
        tlast = request.POST.get('last')
        tdob = request.POST.get('dob')
        temail = request.POST.get('email')
        tmobile = request.POST.get('mobile')
        tskills_list = request.POST.getlist('skills')
        tskills = ','.join(tskills_list)
        tgender = request.POST.get('gender')
        tfile = request.FILES.get('resume')
        user = Login(
            first=tfirst,
            middle=tmiddle,
            last=tlast,
            dob=tdob,
            email=temail,
            mobile=tmobile,
            skills=tskills,
            gender=tgender,
            file=tfile
        )
        user.save()
        print("First:", tfirst)
        print("DOB:", tdob)
        print("Skills:", tskills)
        print("Resume file:", tfile)

        return redirect('home')
    return render(request, "app1/reg.html")
