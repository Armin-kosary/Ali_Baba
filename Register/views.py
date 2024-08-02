from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.request import Request
from .serializers import UserRegistrationSerializer
from User.models import User
from rest_framework import status
from rest_framework.response import Response

# Create your views here.

@api_view(["POST"])
def user_registration_api_view(request: Request):
    if request.method == "POST":
        serializer = UserRegistrationSerializer(data=request.data)

        if serializer.is_valid():
            check_username_availability = User.objects.filter(username = serializer.data["email"]).first()
            
            if check_username_availability:
                return Response({'detail' : 'This Username Is Not Available'}, status.HTTP_406_NOT_ACCEPTABLE)
            
            elif not check_username_availability:
                new_user = User(
                    username = serializer.data["email"],
                    first_name = serializer.data["first_name"],
                    last_name = serializer.data["last_name"],
                )
                new_user.set_password(request.data["password"])
                new_user.save()
                return Response(serializer.data, status.HTTP_201_CREATED)
        
        else:
            return Response({'detail' : 'The Request Was Not Successful'}, status.HTTP_400_BAD_REQUEST)