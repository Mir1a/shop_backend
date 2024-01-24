from ..general import serializers


# class ReadUserSerializer(serializers.UserSerializer):
#     class Meta(serializers.UserSerializer.Meta):
#         fields = serializers.UserSerializer.Meta.fields + ('last_name', 'avatar', 'born')
#
#
# class WriteUserSerializer(serializers.UserSerializer):
#     class Meta(serializers.UserSerializer.Meta):
#         fields = serializers.UserSerializer.Meta.fields + ('password')
#