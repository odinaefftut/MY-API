# urls.py dosyasına aşağıdaki kodu ekleyin
from django.urls import path

from apps.views.userview import UserViewSet, CustomAuthToken

urlpatterns = [
    path('sign_up/', UserViewSet.as_view({'post': 'create'}), name='user-create'),
    path('login/', CustomAuthToken.as_view(), name='user-login'),
]
