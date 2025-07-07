from django.urls import path
from . import views

urlpatterns = [
    path('', views.llm_form, name='llm_form'),
]
