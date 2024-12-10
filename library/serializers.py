from rest_framework import serializers
from .models import Book, BorrowRequest
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

class BorrowRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = BorrowRequest
        fields = '__all__'

class BorrowHistorySerializer(serializers.ModelSerializer):
    book = BookSerializer()

    class Meta:
        model = BorrowRequest
        fields = ['id', 'book', 'start_date', 'end_date', 'status']
