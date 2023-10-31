from rest_framework import serializers

from .models import CustomerDetail

import re


class CustomerDetailsSerlizer(serializers.ModelSerializer):
    class Meta:
        model = CustomerDetail
        fields = "__all__"

    def validate(self, validated_data):
        regex = re.compile("[@_!#$%^&*()<>?/\|}{~:]")
        key_list = validated_data.keys()
        if "name" in key_list:
            if regex.search(validated_data["name"]):
                raise serializers.ValidationError(
                    "name field does not contain special character"
                )
        if "product_name" in key_list:
            if regex.search(validated_data["product_name"]):
                raise serializers.ValidationError(
                    "product_name field does not contain special character"
                )
        if "price" in key_list:
            if validated_data["price"] < 0:
                raise serializers.ValidationError("price should be greater than 0")
        return validated_data
