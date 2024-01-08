from rest_framework import generics, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import SignUpSerializer
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_protect
from django.contrib.auth import authenticate, login
from .models import UserAccount

@method_decorator(csrf_protect, name='dispatch')
class SignUpView(generics.CreateAPIView):
    """
        Validate data and create a new user account if valid.
    """
    serializer_class = SignUpSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            user = UserAccount.objects.create_user(**serializer.validated_data)

            response_data = {
                "message": "User Created Successfully", "data": serializer.data
            }

            return Response(data=response_data, status=200)

        error_data = {"error": serializer.errors}
        return Response(data=error_data, status=400)

@method_decorator(csrf_protect, name='dispatch')
class LoginView(APIView):
    """
        Authenticate the user and log them in.
    """
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        email = request.data['email']
        password = request.data['password']

        user = authenticate(email=email, password=password)
        if user is not None:
            login(request, user)
            return Response({'message': 'Login successful'}, status=200)
        else:
            return Response({'error': 'Invalid credentials'}, status=401)
        
@method_decorator

@method_decorator(ensure_csrf_cookie, name='dispatch')
class GetCSRFToken(APIView):
    """
        Create and set csrf token.
    """
    permission_classes = [permissions.AllowAny]
    def get(self, request, *args, **kwargs):
        return Response({"message": "CSRF successfully set!"}, status=200)