from django.urls import path
from . import views

urlpatterns=[
    path('tweet',views.tw,name="twitter"),
    path('twe',views.twit,name="tweet")
]