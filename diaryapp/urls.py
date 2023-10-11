
from django.urls import path
from .views import *


urlpatterns=[
    path('indexpage/',index),
    path('regi/',reg),
    path('pro/',profile),
    path('editimage/<int:id>', editim),
    path('Logout/',logout_view),
    path('News/',news),
    path('Newsdisp/',newsdisp),
    path('loginind1/',loginind1),
    path('Newsedit/<int:id>',newsedit),
    path('Newsdelete/<int:id>',newsdelete),
    path('adminlogin/',adminlogin),
    path('adminprofile/',adminprofile),
    path('admnNews/',admnnews),
    path('admnNewsdisp/',admnnewsdisp),
    path('admnNewsedit/<int:id>',newseditadmn),
    path('admnNewsdelete/<int:id>',newsdeleteadmn),
    path('Newsuser/',newsuser),
    path('Wishlist/<int:id>',wish),
    path('wishdisp/',wishdis),
    path('editacnt/<int:id>',acntedit),
    path('forgotpassword/',forgot_password),
    path('change/<int:id>',change_password),
    path('check/',check),

]