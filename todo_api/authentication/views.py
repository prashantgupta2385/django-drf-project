
from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from authentication.serializers import RegisterSerializers,LoginSerializer
from rest_framework import response,status,permissions
from django.contrib.auth import authenticate


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

class LoginAPIView(GenericAPIView):
    serializer_class=LoginSerializer
    # permission_classes = [permissions.AllowAny]
    authentication_classes=[]
    def post(self,request):
        email=request.data.get('email',None)
        password=request.data.get('password',None)

        user=authenticate(username=email,password=password)
        
        if user:
            serializer=self.serializer_class(user)

            return response.Response(serializer.data,status=status.HTTP_200_OK)
        return response.Response({'message':"Invalid credential,try again"},status=status.HTTP_401_UNAUTHORIZED)