from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("display/",views.display,name="display"),
    path("alldata2005/", views.all_display, name="all_display"),
]