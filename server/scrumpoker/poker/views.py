from django.template.response import TemplateResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response 
from rest_framework import status
from rest_framework.permissions import IsAuthenticated


def home(request):
    return TemplateResponse(request, 'index.html')

@api_view(['POST'])
def get_logged_user(request):
    return Response(data='works...', status=status.HTTP_200_OK)