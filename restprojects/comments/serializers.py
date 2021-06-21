from rest_framework import serializers
from .models import Comment
from product.models import Product

class CommentSerializer(serializers.Serializer):
    text = serializers.CharField()


class RateSerializer(serializers.Serializer):
    score = serializers.FloatField(min_value=1.0,max_value=5.0)


class ProductDetailSerializer(serializers.ModelSerializer):
    comment_set = CommentSerializer(many=True)

    class Meta:
        model = Product
        fields = ['id', 'name', 'photo','desc','price','avg_score','category','comment_set']

