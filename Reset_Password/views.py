from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.request import Request
from .serializers import ResetPasswordSerializer
from User.models import User
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

@api_view(["PUT"])
def reset_password(request: Request):
    if request.method == "PUT":
        serializer = ResetPasswordSerializer(data=request.data)
        if serializer.is_valid():
            user = request.user
            find_user = User.objects.filter(username = user).first()
            check_old_password = find_user.check_password(serializer.data["old_password"])
            if check_old_password:
                find_user.set_password(serializer.data["new_password"])
                return Response({'detail' : 'Password Reseted'}, status.HTTP_200_OK)
            else:
                return Response({'detail' : 'The Request Was Not Successful'}, status.HTTP_400_BAD_REQUEST)