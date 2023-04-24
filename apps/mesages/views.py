from django.db.models.query import QuerySet

from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework.decorators import action

from mesages.mixins import (
    ResponseMixin,
    ObjectMixin,
)
from mesages.models import (
    Message,
    Chat,
    User
)
from mesages.serializers import (
    MessageSerializer,
    ChatSerializer,
    UserSerializer
)


class MessageViewSet(ResponseMixin, ObjectMixin, ViewSet):
    """ViewSet about chats and messages."""

    queryset: QuerySet[Message] = \
        Message.objects.select_related('to_send').all()

    # list of all
    def list(self, request: Request, *args: tuple) -> Response:
        """GET method."""

        serializer: MessageSerializer = MessageSerializer(
            self.queryset, many=True
        )

        return Response(
            data=serializer.data
        )


class ChatViewSet(ResponseMixin, ObjectMixin, ViewSet):
    """ViewSet about chats."""

    queryset: QuerySet[Chat] = \
        Chat.objects.select_related('owner').all()

    # list of all
    def list(self, request: Request, *args: tuple) -> Response:
        """GET method."""

        serializer: ChatSerializer = ChatSerializer(
            self.queryset, many=True
        )

        return Response(
            data=serializer.data
        )
