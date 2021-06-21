from .views import *
from django.urls import path

urlpatterns = [
    path('category/',CategoryView.as_view()),
    path('category/<str:cat_title>/',CategoryProductView.as_view()),


]