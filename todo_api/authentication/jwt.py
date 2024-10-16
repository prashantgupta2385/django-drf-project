from rest_framework.authentication import get_authorization_header,BaseAuthentication

from rest_framework import exceptions,permissions
import jwt
from django.conf import settings

from authentication.models import User

class JWTAuthentication(BaseAuthentication):
    def authenticate(self,request):
        auth_header=get_authorization_header(request)
        auth_data=auth_header.decode('utf-8')

        auth_token=auth_data.split(" ")

        if len (auth_token)!=2:
            raise exceptions.AuthenticationFailed("Token not valid")

        token=auth_token[1]
        try:
            payload=jwt.decode(token,settings.SECRET_KEY,algorithms=["HS256"])

            username=payload['username']

            user=User.objects.get(username=username)

            return (user,token)
        except jwt.ExpiredSignatureError as ex:
            raise exceptions.AuthenticationFailed('token is expired login again')
        
        except jwt.DecodeError as ex:
            raise exceptions.AuthenticationFailed('token is invalid')
        

        except User.DoesNotExist as no_user:
            raise exceptions.AuthenticationFailed('No such user')
        # return super().authenticate(request)
    


# # authentication/jwt.py

# from rest_framework.authentication import get_authorization_header, BaseAuthentication
# from rest_framework import exceptions
# import jwt
# from django.conf import settings
# from authentication.models import User  # Ensure this points to your User model

# class JWTAuthentication(BaseAuthentication):
#     def authenticate(self, request):
#         auth_header = get_authorization_header(request).decode('utf-8')

#         if not auth_header:
#             return None  # No authentication provided

#         auth_parts = auth_header.split()

#         if len(auth_parts) != 2 or auth_parts[0].lower() != 'bearer':
#             raise exceptions.AuthenticationFailed("Token not valid")

#         token = auth_parts[1]

#         try:
#             payload = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
#             username = payload.get('username')

#             if not username:
#                 raise exceptions.AuthenticationFailed("Invalid token payload.")

#             try:
#                 user = User.objects.get(username=username)
#             except User.DoesNotExist:
#                 raise exceptions.AuthenticationFailed('No such user.')

#             return (user, token)
#         except jwt.ExpiredSignatureError:
#             raise exceptions.AuthenticationFailed('Token has expired. Please log in again.')
#         except jwt.DecodeError:
#             raise exceptions.AuthenticationFailed('Invalid token. Please log in again.')
