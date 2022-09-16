from rest_framework import serializers
from rest_framework.response import Response
from usercontainer.models import RoomManager, User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # exclude = ("",)
        fields = "__all__"

    def create(self, validated_data):
        user = User(**validated_data)
        # user.set_password(validated_data['password'])
        user.save()
        return user

    def get(self, request, *args, **kwargs):
        user = User.objects.get(id=kwargs['id'])
        serializer = UserSerializer(user)
        return Response(serializer.data)



class RoomManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomManager
        fields = '__all__'
