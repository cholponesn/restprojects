from rest_framework.response import Response
from rest_framework import status
from .serializer import *
from rest_framework.views import APIView


class CategoryView(APIView):

    def get(self,request):
        category = Category.objects.all()
        serializers = CategorySerializer(category,many=True)
        return Response(serializers.data,status=status.HTTP_200_OK)

class CategoryProductView(APIView):

    def get(self,request,*args,**kwargs):
        category = Category.objects.get(title=kwargs['cat_title'])
        product_all = category.product_set.all()
        serializer = ProductSerializer(product_all,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
