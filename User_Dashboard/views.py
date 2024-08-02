from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from User.models import User
from .serializers import UserProfileInfoSerializer
# Create your views here.

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def user_profile_info_api_view(request: Request):
    user = request.user
    find_user = User.objects.filter(username = user).first()
    serializer = UserProfileInfoSerializer(find_user)
    return Response(serializer.data, status.HTTP_200_OK)
