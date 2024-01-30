# region				-----External Imports-----
from product.api.general import serializers as product_serializers
# endregion

# region				-----Internal Imports-----
from ..general import serializers as general_serializers
from ... import models as user_models
# endregion


class ReadUserSerializer(general_serializers.UserSerializer):
    favorites = product_serializers.ItemSerializer(many=True, read_only=True)
    class Meta(general_serializers.UserSerializer.Meta):
        fields = general_serializers.UserSerializer.Meta.fields\
                 + ('email', 'last_name', 'avatar', 'born', 'favorites')



class WriteUserSerializer(general_serializers.UserSerializer):
    class Meta(general_serializers.UserSerializer.Meta):
        fields = general_serializers.UserSerializer.Meta.fields\
                 + ('last_name', 'born')


class RegisterUserSerializer(general_serializers.UserSerializer):
    class Meta(general_serializers.UserSerializer.Meta):
        fields = general_serializers.UserSerializer.Meta.fields\
                 + ('email', 'password', 'last_name', 'born')

    # region      -----Internal Methods-----
    def create(self, validated_data):
        user = user_models.User.objects.create(**validated_data)
        user.set_password(validated_data["password"])
        user.save()
        return user
    # endregion

