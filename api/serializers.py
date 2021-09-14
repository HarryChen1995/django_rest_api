from rest_framework import serializers
from .models import Message
from django.contrib.auth.models import User
class MessageSerializer(serializers.Serializer):
    is_incomming = serializers.BooleanField()
    content = serializers.CharField(max_length=30)
    created = serializers.DateTimeField()
    def create(self, validated_data):
        return Message.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.is_incomming = validated_data.get('is_incomming', instance.is_incomming)
        instance.content = validated_data.get('content', instance.content)
        instance.created = validated_data.get('created', instance.created)
        instance.save()
        return instance



class UserSerilizer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

