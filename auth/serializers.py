from rest_framework.serializers import ModelSerializer
from rest_framework_simplejwt.tokens import Token
class TokenSerizlier(ModelSerializer):
    class Meta:
        model = Token
        fields = "__all__"