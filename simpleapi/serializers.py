from django.db.models import fields
from rest_framework import serializers
from tests.models import *


class UIIDSerializer(serializers.ModelSerializer):
    class Meta:
        model = KeyValue
        fields = "__all__"