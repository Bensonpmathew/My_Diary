from django.db import models

# Create your models here.

class regmod1(models.Model):

    uname = models.CharField(max_length=30)
    num=models.IntegerField()
    em=models.EmailField()
    im=models.FileField(upload_to='diaryapp/static')
    pin=models.CharField(max_length=30) #int(pin) views il vilikkanam
    def __str__(self):
        return self.uname

class logmod1(models.Model):
    uname=models.CharField(max_length=30)
    pswd=models.CharField(max_length=30)

class newsmodel(models.Model):
    topic=models.CharField(max_length=30)
    content = models.CharField(max_length=3000)
    date=models.DateField(auto_now_add=True)


class admnnewsmodel(models.Model):
    topic=models.CharField(max_length=30)
    content = models.CharField(max_length=3000)
    date=models.DateField(auto_now_add=True)

class wishlist(models.Model):
    uid = models.IntegerField()
    admnnewsid=models.IntegerField()
    topic = models.CharField(max_length=30)
    content = models.CharField(max_length=3000)
    date = models.DateField()