from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name='home'),
    path('htm',views.htm,name='html'),
    path('fb',views.fb,name="facebook")
]