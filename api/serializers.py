from rest_framework import serializers
from .models import *
from rest_framework.serializers import ModelSerializer


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = [
            'name',
            'description'
        ]


class ItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = Item
        fields = [
            'name',
            'description',
            'category',
            'price',
            'qty',
        ]

class MenuSerializer(serializers.ModelSerializer):

    class Meta:
        model = Menu
        fields = [
            'name',
            'item'
        ]


class RestaurantSerializer(serializers.ModelSerializer):

    class Meta:
        model = Restaurant
        fields = [
            'name',
            'description',
            'location',
            'menu',
        ]


