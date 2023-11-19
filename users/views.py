from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.exceptions import AuthenticationFailed

from users.serializers import LoginSerializer, UserSerializer

class SignUpView(generics.CreateAPIView):
    """Sign up users view"""
    serializer_class = UserSerializer


class LoginView(TokenObtainPairView):
    """Login users view"""
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except AuthenticationFailed as e:
            return Response(str(e), status=status.HTTP_401_UNAUTHORIZED)

        return super().post(request, *args, **kwargs)


class LogoutView(APIView):
    """Logout view user"""
    permission_classes = (IsAuthenticated, )

    def post(self, request):
        """process the logout method from received data"""
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class HomeView(APIView):
    """Home view for the API"""
    # permission_classes = (IsAuthenticated, )

    def get(self, request):
        """get method that returns a message"""
        content = {
            'message': 'Welcome to Indices Trade Lab API. Visit `/docs/` to view how to use the api!',
        }
        return Response(content)
