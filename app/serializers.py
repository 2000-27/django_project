from rest_framework import serializers

from .models import CustomerDetail

import re


class CustomerDetailsSerlizer(serializers.ModelSerializer):
    class Meta:
        model = CustomerDetail
        fields = "__all__"

    def validate(self, validated_data):
        name = validated_data["name"]
        if validated_data.get("name"):
            regex = re.compile("[@_!#$%^&*()<>?/\|}{~:]")
            if not regex.search(name) is None:
                raise serializers.ValidationError(
                    "name does not contain special character"
                )
            if not regex.search(validated_data["product_name"]) is None:
                raise serializers.ValidationError(
                    "price does not contain special character"
                )
            if validated_data["price"] < 0:
                raise serializers.ValidationError("price should be greater than 0")
        return validated_data
