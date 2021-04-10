from django.urls import path
from .views import ImageRecognition
from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('image/', ImageRecognition.as_view()),
]