# api/authentication.py

from rest_framework.authentication import BaseAuthentication
from rest_framework import exceptions
from clerk_backend_api import Clerk
from clerk_backend_api.security import AuthenticateRequestOptions
from django.conf import settings
from django.contrib.auth.models import User

class ClerkAuthentication(BaseAuthentication):
    def authenticate(self, request):
        auth_header = request.headers.get('Authorization')
        if not auth_header or not auth_header.startswith('Bearer '):
            return None

        token = auth_header.split(' ')[1]
        sdk = Clerk(bearer_auth=settings.CLERK_SECRET_KEY)

        options = AuthenticateRequestOptions(authorized_parties=[settings.FRONTEND_ORIGIN])
        auth_state = sdk.authenticate_request(request, options)

        if not auth_state.is_signed_in:
            raise exceptions.AuthenticationFailed("Invalid or expired Clerk token")

        # Use the user id from the auth_state.payload
        user_id = auth_state.payload.get('sub')
        if not user_id:
            raise exceptions.AuthenticationFailed("No user ID in token")

        user, _ = User.objects.get_or_create(username=user_id)
        return (user, None)
