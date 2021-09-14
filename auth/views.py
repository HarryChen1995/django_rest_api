from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse
import json
from django.contrib.auth import authenticate, login, logout
from rest_framework_simplejwt.tokens import RefreshToken

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


@csrf_exempt
def login_user(request):
    data = json.loads(request.body)
    username = data["username"]
    password = data["password"]
    
    user = authenticate(request, username = username, password = password)
    if user is not None:
        login(request, user)
        return JsonResponse(get_tokens_for_user(user))
    else:
        return JsonResponse({"message":"login failed !"}, status = 403)



@csrf_exempt
def logout_user(request):
    logout(request)
    return JsonResponse({"message":"you are logged out !"})

@csrf_exempt
def signup(request):
    data = json.loads(request.body)
    firstname = data["firstname"]
    lastname = data["lastname"]
    username  = data["username"]
    email = data["email"]
    pasword = data["password"]
    if User.objects.filter(first_name = firstname,last_name = lastname).exists() or User.objects.filter(username = username).exists() or User.objects.filter(email = email).exists():
        return JsonResponse({"message":"User already exist"})
    else:
        user = User.objects.create_user(first_name = firstname, last_name = lastname, username = username, email = email, password = pasword)
        return JsonResponse({"message":"User Created !"})
        