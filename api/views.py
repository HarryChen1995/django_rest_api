# Create your views here.
from django.contrib.auth.models import  User, Group
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from .serializers import *
from .models import *
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
class CommentView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        comment = Comment(email='foo@example.com', content='foo bar')
        comment.save()
        serializer = CommentSerializer(comment)
        return Response(serializer.data)