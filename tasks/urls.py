from django.urls import path, include
from rest_framework.routers import DefaultRouter
from tasks.views import TaskViewSet, RegisterUser, LoginUser

router = DefaultRouter()
router.register(r'tasks', TaskViewSet)

urlpatterns = [
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', LoginUser.as_view(), name='login'),
    path('', include(router.urls)),
]
