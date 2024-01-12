from django.urls import path
# from . import views
from .views import test_backend, get_user_info

# urlpatterns = [
#     path('hello-world', views.hello_world, name='hello_world')
# ]

urlpatterns = [
    path('test-backend/', test_backend, name='test_backend'),
    path('api/get_user_info/', get_user_info, name='get_user_info'),
    # path('dashboard/', views.dashboard, name='dashboard')
]

