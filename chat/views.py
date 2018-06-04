# chat/views.py
import json
from django.shortcuts import render
from django.utils.safestring import mark_safe

#rest-framework
from rest_framework import status
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import authentication_classes, permission_classes

# custom libraty
import message_constants
from lib.util import custom_render_data, SkipAuth

from .serializers import *

def index(request):
    return render(request, 'chat/base.html', {})

def room(request, room_name, token):
    # print("Swaraj in views", token)
    return render(request, 'chat/room.html', {
        'room_name_json' : mark_safe(json.dumps(room_name)),
        'token' : mark_safe(json.dumps(token))
    })

class Signup(APIView):
    """
    user can register his detail and able to login in system.
    """
    # @permission_classes([SkipAuth])
    # @permission_classes([])
    permission_classes = []
    def post(self, request):
        try:
            print("*****", request.data)
            if 'email' in request.data:
                request.data['username'] = request.data['email']
            if not User.objects.filter(email__iexact=request.data['email']).exists():
                user_serializer = UserSerializer(data=request.data)
                if user_serializer.is_valid():
                    user = user_serializer.create(request.data)
                    token  = Token.objects.create(user = user)
                    return Response({'status': status.HTTP_200_OK,'data' :user_serializer.data, 'token': token.key})
                return Response({'status': status.HTTP_400_BAD_REQUEST,
                    'message': 'Please provided required fields.',
                    'error' : user_serializer.errors,})    
            else :
                return Response({'status': status.HTTP_400_BAD_REQUEST,
                    'message': 'Email alredy exists.',
                    })
        except Exception as e:
            print("EEEEEEEE", e)
            return Response({'status': status.HTTP_400_BAD_REQUEST,
                'message': "Data validation error.",
                })
            
