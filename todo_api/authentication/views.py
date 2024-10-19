
from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from authentication.serializers import RegisterSerializers,LoginSerializer
from rest_framework import response,status,permissions
from django.contrib.auth import authenticate
from rest_framework.views import APIView






# Create your views here.

class AuthuserAPIView(GenericAPIView):
    permission_classes=(permissions.IsAuthenticated,)

    def get(self,request):
        user=request.user
        serializer=RegisterSerializers(user)
        return response.Response({'user':serializer.data})


class RegisterAPIView(GenericAPIView):
    serializer_class=RegisterSerializers
    authentication_classes=[]
    # permission_classes = [permissions.AllowAny]
    def post(self,request):
        serializer=self.serializer_class(data=request.data)



        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data,status.HTTP_201_CREATED)
        return response.Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
from rest_framework import response  # Ensure you're importing the response module

class LoginAPIView(GenericAPIView):
    serializer_class = LoginSerializer
    authentication_classes = []

    def post(self, request):
        email = request.data.get('email', None)
        password = request.data.get('password', None)

        user = authenticate(username=email, password=password)


        if user:
            serializer=self.serializer_class(user)

            return response.Response(serializer.data,status=status.HTTP_200_OK)
        return response.Response({'message':"Invalid credential,try again"},status=status.HTTP_401_UNAUTHORIZED)
    

#  # Initialize a local variable for the response
#         login_response = response.Response(status=status.HTTP_400_BAD_REQUEST)

#         if user:
#             serializer = self.serializer_class(user)

#             # Set the JWT token as an HTTP-only cookie
#             response_data = serializer.data
#             login_response = response.Response(response_data, status=status.HTTP_200_OK)
#             login_response.set_cookie(
#                 key='jwt',
#                 value=user.token,  # Get the JWT token from the user model
#                 httponly=True,      # Ensure the cookie is HTTP-only for security
#                 samesite='Lax'      # Optional: control how cookies are sent (for CSRF protection)
#             )
#         else:
#             # If authentication fails, set a message in the response
#             login_response.data = {'message': "Invalid credentials, try again."}

#         return login_response



        if user:
            serializer=self.serializer_class(user)

            return response.Response(serializer.data,status=status.HTTP_200_OK)
        return response.Response({'message':"Invalid credential,try again"},status=status.HTTP_401_UNAUTHORIZED)
    

# class LogoutAPIView(APIView):
#     permission_classes = [permissions.IsAuthenticated]

#     def post(self, request):
#         # Initialize a local variable for the response
#         logout_response = response.Response({"message": "Successfully logged out"}, status=status.HTTP_200_OK)
        
#         # Remove the 'jwt' cookie from the client
#         logout_response.delete_cookie('jwt')
        
#         return logout_response


       