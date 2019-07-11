from django.conf.urls import url
from firstapp import views


app_name='firstapp'

urlpatterns=[
    url(r'^feedback/$',views.feedback,name='feedback'),
    url(r'^reg/$',views.reg,name='reg'),
    url(r'^$',views.index,name='index'),
]