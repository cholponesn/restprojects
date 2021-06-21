from django.urls import path
from .views import *


urlpatterns = [path ( 'order/',OrderPostView.as_view()),
               path ('my_orders/',MyOrderView.as_view()),
               path ('my_orders/<int:order_id>/',UpdateDeleteOrder.as_view()),

]