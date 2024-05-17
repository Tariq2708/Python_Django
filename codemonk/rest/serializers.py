from rest_framework import serializers
from .models import CustomUser, Paragraph, WordToParagraphMapping

# Serializer for the CustomUser model
class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'name', 'dob', 'created_at', 'modified_at']

# Serializer for user registration and management
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['email', 'name', 'dob', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        # Custom user creation logic
        user = CustomUser.objects.create_user(**validated_data)
        return user

# Serializer for the Paragraph model
class ParagraphSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paragraph
        fields = ['id', 'text', 'created_at', 'modified_at']

# Serializer for the WordToParagraphMapping model
class WordToParagraphMappingSerializer(serializers.ModelSerializer):
    class Meta:
        model = WordToParagraphMapping
        fields = ['id', 'word', 'paragraph', 'created_at', 'modified_at']
