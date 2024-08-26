
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import Outfit, User
from .serializer import OutfitSerializer, UserSerializer
from django.contrib.auth import authenticate, login, logout
from rest_framework.views import APIView
from django.views.decorators.csrf import csrf_exempt
from django.middleware.csrf import get_token
from django.http import JsonResponse

class UserListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class UserRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

class OutfitListCreateView(generics.ListCreateAPIView):
    queryset = Outfit.objects.all()
    serializer_class = OutfitSerializer

class OutfitDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Outfit.objects.all()
    serializer_class = OutfitSerializer

class UserSessionCheckView(APIView):
    def get(self, request, *args, **kwargs):
       
        if request.user.is_authenticated:
           
            return Response({'message': 'User is authenticated', 'username': request.user.username}, status=status.HTTP_200_OK)
        else:
           
            return Response({'message': 'User is not authenticated'}, status=status.HTTP_401_UNAUTHORIZED)
            
class UserLoginView(APIView):
    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return Response({'message': 'Login successful', 'username': user.username}, status=status.HTTP_200_OK)
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)

class UserLogoutView(APIView):
    def post(self, request, *args, **kwargs):
        logout(request)
        return Response({'message': 'Logout successful'}, status=status.HTTP_200_OK)

def csrf_token_view(request):
    token = get_token(request)
    return JsonResponse({'csrfToken': token})