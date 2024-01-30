from rest_framework import serializers
from ...models import User


class UserSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=5, read_only=True)

    class Meta:
        model = User
        fields = ('id', 'name', 'email', 'password')


    # region      -----Internal Methods-----
    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        user.set_password(validated_data["password"])
        user.save()
        return user
    # endregion

