from rest_framework import serializers
import re
from .models import DullAPI, BlockList

class DullSerializer(serializers.ModelSerializer):

    class Meta:

        model = DullAPI
        fields = [
            "name", "description"
        ]

class BlockListSerializer(serializers.ModelSerializer):

    class Meta:

        model = BlockList
        fields = [
            "ip_address"
        ]

    def validate_ip_address(self, value):
        if bool(re.search("^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$", value)):
            return value
        else:
            return serializers.ValidationError("Invalid ip")


