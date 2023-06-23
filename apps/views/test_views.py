from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from apps.models.test_models import TestModel
from apps.serializers.test_serializers import TesrModelSerializer


# class TestModelView(generics.RetrieveUpdateAPIView):
#     queryset = TestModel.objects.all()
#     serializer_class = TesrModelSerializer
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]
#
#     def get(self, request, *args, **kwargs):
#         if not request.user.is_authenticated:
#             return self.retrieve(request, *args, **kwargs)
#         else:
#             return Response("Only authenticated users can update the data.", status=status.HTTP_403_FORBIDDEN)
#
#     def put(self, request, *args, **kwargs):
#         if request.user.is_authenticated:
#             return self.update(request, *args, **kwargs)
#         else:
#             return Response("Only authenticated users can update the data.", status=status.HTTP_403_FORBIDDEN)
#
#     def patch(self, request, *args, **kwargs):
#         if request.user.is_authenticated:
#             return self.partial_update(request, *args, **kwargs)
#         else:
#             return Response("Only authenticated users can update the data.", status=status.HTTP_403_FORBIDDEN)

# http_method_names = ['get', ]

class TestModelViewSet(viewsets.ModelViewSet):
    queryset = TestModel.objects.all()
    serializer_class = TesrModelSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]



