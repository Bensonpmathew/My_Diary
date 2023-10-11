from django import forms


class regform1(forms.Form):

    uname = forms.CharField(max_length=30)
    num=forms.IntegerField()
    em=forms.EmailField()
    im=forms.FileField()
    pin=forms.CharField(max_length=30)
    cpin = forms.CharField(max_length=30)



class logform1(forms.Form):
    uname=forms.CharField(max_length=30)
    pin=forms.CharField(max_length=30)

class newsform(forms.Form):
    topic=forms.CharField(max_length=300)
    content = forms.CharField(max_length=3000)
    # date=forms.DateField(auto_now_add=True)

class adminform(forms.Form):
    username=forms.CharField(max_length=30)
    # email=forms.EmailField()
    password=forms.CharField(max_length=30)

class admnnewsform(forms.Form):
    topic=forms.CharField(max_length=300)
    content = forms.CharField(max_length=3000)
    # date=forms.DateField(auto_now_add=True)