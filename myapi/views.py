# from django.shortcuts import render
# from rest_framework.decorators import api_view
# from rest_framework.response import Response

from django.http import JsonResponse

def test_backend(request):
  return JsonResponse({'message': 'Backend connection successful!'})
# Create your views here.
# @api_view(['GET'])
# def hello_world(request):
#   return Response({'message': 'Hello, World!'})