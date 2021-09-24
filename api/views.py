# Create your views here.
from django.http.response import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from .models import *
from rest_framework.permissions import IsAuthenticated
class MessageView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        message = Message(content='foo bar')
        message.save()
        serializer = MessageSerializer(message)
        return Response(serializer.data)




def index(request):
    if request.user.is_authenticated:
        user = request.user
        serializer = UserSerilizer(user)
        return JsonResponse(serializer.data)
    else:
        return JsonResponse({"message":"your are not logged in !"}, status = 401)

    


