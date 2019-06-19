from rest_framework import serializers
from .models import UserTrueAndFalse



class UserTrueAndFalseSerializer2(serializers.ModelSerializer):

    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    class Meta:
        model = UserTrueAndFalse
        fields = '__all__'


