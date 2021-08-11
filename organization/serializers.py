from rest_framework import serializers
from . import models


class OrganizationSerializer(serializers.ModelSerializer):
    """
         Serializer class form Organization
    """

    class Meta:
        model = models.OrganizationInfo
        fields = (
            'name',
            'city',
            'number',
            'email',
            'number_of_employees',
            'related_product',
            'introducer_name',
            'introducer_number',
            'operator_info',
            'created_info',
        )
 # "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTYyODc5MjQwNCwianRpIjoiODUzZGEzY2Y0YWU0NDZjMDg1NjczN2U2NzE4ZWIxODUiLCJ1c2VyX2lkIjoxfQ.G5q3xELmRUPoSINswSCOptQNjm5LaWS-kIT5MIAoQCQ",
 #    "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjI4NzA2MzA0LCJqdGkiOiJlYzRmMjUyMzc4NGQ0OGVlYTNlYzdhZWM3ZTIyYWMzYSIsInVzZXJfaWQiOjF9.bT4gtJfcIpzckaJIJ-NGwCjUVKBwQ21yeU0DqTZR6Eo"