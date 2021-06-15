from .views import *
from django.urls import path
urlpatterns = [
    path('category/',CategoryView.as_view())

]