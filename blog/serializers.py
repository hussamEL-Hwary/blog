from rest_framework import serializers
from .models import Category, Tutorial

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class TutorialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tutorial
        fields = ('slug', 'title', 'min_read', 'created_at', 'updated_at', 'category', 'img_url', 'content')
