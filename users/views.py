from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from .serializers import RegisterSerializer

# Create your views here.
class RegisterView(APIView):

    def post(self,request):
        serializer=RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"User Register Successfully!!!","user":serializer.data},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class LoginView(APIView):

    def post(self,request):
        username=request.data.get('username')
        password=request.data.get('password')

        user=authenticate(username=username,password=password)
        if user is not None:
            refresh=RefreshToken.for_user(user)
            return Response({"message":"Login successfully!!!","access":str(refresh.access_token),"refresh":str(refresh)},status=status.HTTP_200_OK)
        return Response({"error":"Invalid Username or password"},status=status.HTTP_401_UNAUTHORIZED)
