from django.shortcuts import render
from django.http import HttpResponse
import os

from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import *
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

from django.core.mail import send_mail
from django.contrib.auth import logout


# Create your views here.

def index(request):
    return render(request,'index.html')


#
# def reg(request):
#     return render(request,'registration.html')

def reg(request):
    if request.method == 'POST':
        a = regform1(request.POST, request.FILES)
        if a.is_valid():
            un = a.cleaned_data['uname']
            nm = a.cleaned_data['num']
            em = a.cleaned_data['em']
            im = a.cleaned_data['im']
            ps = a.cleaned_data['pin']
            cps = a.cleaned_data['cpin']

            if ps == cps:
                b = regmod1( uname=un, num=nm, em=em, im=im, pin=ps, )
                b.save()
                subject = '$$$  ACCOUNT CREATION SUCCESS $$$'
                message = 'YOUR NEW MY DIARY ACCOUNT HAS BEEN CREATED SUCCESSFULLY '  # formatter used for variable recognition
                email_from = "techymech23@gmail.com"
                email_to = 'bensonpm333@gmail.com'
                send_mail(subject, message, email_from, [email_to])
                return redirect(loginind1)
            else:
                return HttpResponse('PASSWORD MISMATCH !')
        else:
            return HttpResponse('REGISTRATION FAILED !!!')
    return render(request, 'registration.html')


# def login(request):
#     return render(request,'login.html')



# def login(request):
#     if request.method == 'POST':
#         a = logform1(request.POST)
#         if a.is_valid():
#             un = a.cleaned_data['uname']
#             ps = a.cleaned_data['pswd']
#
#             b = regmod1.objects.all()
#             for i in b:
#                 if i.uname == un and i.pin == ps:
#                     request.session['id'] = i.id  # global calling  (global variable-->request.session['id])
#                     return redirect(profile)
#             else:
#                 return HttpResponse('Password missmatch')
#         else:
#             return HttpResponse('INVALID')
#     return render(request, 'login.html')

def loginind1(request):
    if request.method=='POST':
        a=logform1(request.POST)
        if a.is_valid():
            nm=a.cleaned_data['uname'] #green clr->form & orange->models
            ps=a.cleaned_data['pin']
            b=regmod1.objects.all() #registraion nte models.py file
            for i in b:
                if i.uname==nm and i.pin==ps:
                    request.session['id'] = i.id
                    return redirect(profile)
            else:
                return HttpResponse ('LOGIN FAILED')
        else:
            return HttpResponse(index)

    return render(request,'loginind1.html')



# def profile(request):
#     return render(request,'profile.html')
def profile(request):
    id1 = request.session['id']
    a = regmod1.objects.get(id=id1)
    im = str(a.im).split('/')[-1]  # splitting file path
    return render(request, 'profile.html', {'a': a, 'im': im})






def editim(request, id):
    a = regmod1.objects.get(id=id)
    im = str(a.im).split('/')[-1]
    if request.method == 'POST':
        a.uname = request.POST.get('uname')
        if len(request.FILES) != 0:
            if len(a.im) > 0:
                os.remove(a.im.path)
            a.im = request.FILES['im']
        a.save()
        return redirect(profile)
    return render(request, 'imgedit.html', {'a': a, 'im': im})



def logout_view(request):
    logout(request)
    return redirect(index)



def newsdisp(request):  # admin
    a = newsmodel.objects.all()
    return render(request, 'newsdisp.html', {'a': a})


def news(request):
    if request.method == 'POST':
        a = newsform(request.POST, request.FILES)
        if a.is_valid():
            to = a.cleaned_data['topic']
            cnt = a.cleaned_data['content']
            b = newsmodel(topic=to, content=cnt)
            b.save()
            return redirect(profile)
        else:
            return HttpResponse('FAILURE!!!')
    return render(request, 'news.html')



def newsedit(request, id):
    a = newsmodel.objects.get(id=id)
    if request.method == 'POST':
        a.topic = request.POST.get('topic')
        a.content = request.POST.get('content')
        a.save()
        return redirect(newsdisp)
    return render(request, 'newsedit.html', {'a': a})


def newsdelete(request, id):
    a = newsmodel.objects.get(id=id)
    a.delete()
    return redirect(newsdisp)


def adminlogin(request):
    if request.method == 'POST':
        a = adminform(request.POST)
        if a.is_valid():
            us = a.cleaned_data['username']

            ps = a.cleaned_data['password']
            user = authenticate(request, username=us, password=ps)
            if user is not None:
                return redirect(adminprofile)
            else:
                return HttpResponse('Failed !!')

    return render(request, 'adminlogin.html')


def adminprofile(request):
    return render(request, 'adminprofile.html')

def admnnewsdisp(request):  # admin
    a = admnnewsmodel.objects.all()
    return render(request, 'admnnewsdisp.html', {'a': a})

def admnnews(request):
    if request.method == 'POST':
        a = admnnewsform(request.POST, request.FILES)
        if a.is_valid():
            to = a.cleaned_data['topic']
            cnt = a.cleaned_data['content']
            b = admnnewsmodel(topic=to, content=cnt)
            b.save()
            return redirect(admnnewsdisp)
        else:
            return HttpResponse('FAILURE!!!')
    return render(request, 'adminnews.html')


def newseditadmn(request, id):
    a = admnnewsmodel.objects.get(id=id)
    if request.method == 'POST':
        a.topic = request.POST.get('topic')
        a.content = request.POST.get('content')
        a.save()
        return redirect(admnnewsdisp)
    return render(request, 'admnnewsedit.html', {'a': a})


def newsdeleteadmn(request, id):
    a = admnnewsmodel.objects.get(id=id)
    a.delete()
    return redirect(admnnewsdisp)


def newsuser(request):
    a = admnnewsmodel.objects.all()
    return render(request, 'newsuser.html', {'a': a})


def wish(request, id):
    a = admnnewsmodel.objects.get(id=id)
    a1 = wishlist.objects.all()
    for i in a1:
        if i.admnnewsid == a.id and i.uid == request.session[
            'id']:  # wishlist ilai item equal aanennum athinte uid um login cheytha uid um equal aayaal mathram msg kaanichaal mathi
            return render(request,'already.html')
    b = wishlist(topic=a.topic, content=a.content, date=a.date, admnnewsid=a.id, uid=request.session['id'])
    b.save()
    return render(request,'added wish.html')


def wishdis(request):
    try:
        a = wishlist.objects.all()
        id = request.session['id']
        return render(request, 'wishlist.html', {'a': a, 'id': id})
    except:
        return redirect(loginind1)

def acntedit(request, id):
    a = regmod1.objects.get(id=id)
    if request.method == 'POST':
        a.uname = request.POST.get('uname')
        a.num = request.POST.get('num')
        a.em = request.POST.get('em')
        a.pin = request.POST.get('pin')
        a.save()
        return redirect(profile)
    return render(request, 'editaccount.html', {'a': a})



def forgot_password(request):
    a=regmod1.objects.all()
    if request.method=='POST':
        em= request.POST.get('em')
        num= request.POST.get('num')
        for i in a:
            if(i.em==em and i.num==int(num)):

                id=i.id
                subject="Password Change"
                message=f"http://127.0.0.1:8000/diaryapp/change/{id}"
                # message="Renew your password"
                frm="techymech23@gmail.com"
                to=em
                send_mail(subject,message,frm,[to])
                return redirect(check)
        else:
            return HttpResponse("Sorry, Some Error Occured")
    return render(request,'forgotpass.html')


def change_password(request,id):
    a=regmod1.objects.get(id=id)
    if request.method=='POST':
        p1=request.POST.get('pin')
        p2=request.POST.get('repin')
        if p1==p2:
            a.pin=p1
            a.save()
            return HttpResponse('Password changed')
        else:
            return HttpResponse('Sorry!!')
    return render(request,'changepass.html')


def check(request):
    return render(request,'checkemail.html')

