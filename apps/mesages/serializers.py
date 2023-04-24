from rest_framework import serializers
from django.contrib.auth.models import User

from mesages.models import Chat


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class MessageSerializer(serializers.Serializer):
    """
    Serializer for getting all messages fields.
    """

    sender: User = UserSerializer()
    to_send: Chat = serializers.PrimaryKeyRelatedField(
        queryset=Chat.objects.all()
    )
    text = serializers.CharField()
    datetime_send = serializers.DateTimeField()

    class Meta:
        fields = (
            'sender',
            'to_send',
            'text',
            'datetime_send'
        )

    def validate(self, attrs):
        # Если to_send не является групповым чатом, то кол-во участников должно быть обязательно быть равно 1
        if attrs.get("text") == "":
            raise ValueError('GG')
        return attrs

    # def validate_to_send(self, value):
    #     chat = Chat.objects.get(id=value.id)
    #     if not chat.is_group_chat and chat.members.count() != 1:
    #         raise serializers.ValidationError(
    #             "Only one member allowed in non-group chats")
    #     return value


class ChatSerializer(serializers.Serializer):
    """
    Serializer for getting all chat fields.
    """

    owner: User = UserSerializer(required=False)
    is_many = serializers.BooleanField(read_only=True)
    name = serializers.CharField()
    members: User = UserSerializer(
        many=True
    )

    class Meta:
        fields = (
            'owner',
            'is_many',
            'name',
            'members'
        )


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for get all user data
    """

    class Meta:
        model = User
        fields = ('__all__',)
