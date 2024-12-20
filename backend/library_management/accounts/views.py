from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import CustomUserSerializer
from .models import CustomUser
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken

class UserRegistrationView(APIView):
    permission_classes = [AllowAny]  # Allow anyone to register (no token verification)

    def post(self, request):
        user_type = request.data.get('type')
        if not user_type:
            return Response({"error": "The 'type' field is required."}, status=status.HTTP_400_BAD_REQUEST)

        email = request.data.get('email')
        if not email:
            return Response({"error": "The 'email' field is required."}, status=status.HTTP_400_BAD_REQUEST)

        # Skip token-based authentication, allow everyone to register (no restriction based on user_type)
        if user_type not in ['admin', 'staff', 'borrower']:
            return Response({"error": "Invalid user type."}, status=status.HTTP_400_BAD_REQUEST)

        # Prepare user data for creation
        data = {
            'username': request.data.get('username'),
            'email': email,
            'password': request.data.get('password'),
            'type': user_type,
        }

        serializer = CustomUserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()  # Save the user
            return Response({"message": "User created successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    permission_classes = [AllowAny]  # Unauthenticated users can access this

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        # Ensure both username and password are provided
        if not username or not password:
            return Response({"detail": "Username and password are required."}, status=status.HTTP_400_BAD_REQUEST)

        # Authenticate the user
        user = authenticate(request, username=username, password=password)

        if user is not None:
            if user.is_active:
                # Create and return tokens
                refresh = RefreshToken.for_user(user)
                access_token = str(refresh.access_token)
                return Response({
                    'refresh': str(refresh),
                    'access': access_token,
                    'user': {
                        'username': user.username,
                        'type': user.type,
                    }
                }, status=status.HTTP_200_OK)
            else:
                return Response({"detail": "User account is deactivated."}, status=status.HTTP_403_FORBIDDEN)
        else:
            return Response({"detail": "Invalid username or password."}, status=status.HTTP_401_UNAUTHORIZED)