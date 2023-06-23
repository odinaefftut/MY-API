from rest_framework import serializers

from apps.models.test_models import TestModel


class TesrModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestModel
        fields = ('id', 'title', 'description', 'image')
