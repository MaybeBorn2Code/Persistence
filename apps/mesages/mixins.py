from rest_framework.response import Response

from django.db.models import QuerySet

from typing import Any


class ObjectMixin:
    """ObjectMixin."""

    def get_object(
        self,
        queryset: QuerySet[Any],
        obj_id: str
    ) -> Any:
        obj: Any = None
        try:
            obj = queryset.get(id=obj_id)
        except Exception as exc:
            print(f'ERROR.ObjectMixin.get_object: {exc}')
            return None
        else:
            return obj


class ResponseMixin:
    """ResponseMixin."""

    def get_json_response(
        self,
        data: dict[str, Any],
        key_name: str = 'default',
    ) -> Response:

        return Response(
            {
                'data': {
                    key_name: data
                }
            }
        )
