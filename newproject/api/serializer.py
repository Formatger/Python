from rest_framework import serializers
from .models import User
from .models import Confeccion

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class ConfeccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Confeccion
        fields = '__all__'