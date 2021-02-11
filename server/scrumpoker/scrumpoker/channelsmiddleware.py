from rest_framework_simplejwt.tokens import UntypedToken
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from jwt import decode as jwt_decode
from django.conf import settings
from django.contrib.auth import get_user_model
from urllib.parse import parse_qs
from channels.db import database_sync_to_async


class TokenAuthMiddleware:

    def __init__(self, app):
        self.app = app


    @database_sync_to_async
    def get_user(self, user_id):
        return get_user_model().objects.filter(id=user_id).first()


    async def __call__(self, scope, receive, send):
        qs = parse_qs(scope["query_string"].decode("utf8"))
        token = qs.get("token", [""])[0]

        try:
            UntypedToken(token)
        except (InvalidToken, TokenError) as e:
            return None

        decoded_data = jwt_decode(token, settings.SECRET_KEY, algorithms=["HS256"])
        scope["user"] = await self.get_user(int(decoded_data["user_id"]))
        return await self.app(scope, receive, send)