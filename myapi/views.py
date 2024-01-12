# from django.shortcuts import render
# from rest_framework.decorators import api_view
# from rest_framework.response import Response

from django.http import JsonResponse
from appwrite.services.account import Account
from appwrite.client import Client

appwrite_client = Client()
appwrite_client.set_endpoint('API_ENDPOINT')
appwrite_client.set_project('PROJECT_ID')
appwrite_client.set_key('SECRET_API_KEY')

def get_user_info(request):
  user_info = Account(appwrite_client).get()
  return JsonResponse({'user_info': user_info})

def test_backend(request):
  return JsonResponse({'message': 'Backend connection successful!'})
# Create your views here.
# @api_view(['GET'])
# def hello_world(request):
#   return Response({'message': 'Hello, World!'})

