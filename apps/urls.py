# urls.py
from django.urls import path,include
from rest_framework.routers import DefaultRouter

from apps.views.test_views import  TestModelViewSet
from apps.views.userview import UserViewSet, CustomAuthToken

router = DefaultRouter()
router.register(r'test_models', TestModelViewSet)

urlpatterns = [
    path('api/', include(router.urls)),

    path('sign_up/', UserViewSet.as_view({'post': 'create'}), name='user-create'),
    path('login/', CustomAuthToken.as_view(), name='user-login'),

    # path('test/<int:pk>/', TestModelView.as_view(), name='test-model-detail'),


]
