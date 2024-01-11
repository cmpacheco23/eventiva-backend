from django.urls import path
# from . import views
from .views import test_backend

# urlpatterns = [
#     path('hello-world', views.hello_world, name='hello_world')
# ]

urlpatterns = [
    path('test-backend/', test_backend, name='test_backend')
]

