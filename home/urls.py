from django.urls import path
from home.views import homeView
from . import views

urlpatterns = [
    path('',homeView.as_view(), name='home'),

]