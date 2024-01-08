from rest_framework import generics, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import SignUpSerializer
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_protect
from django.middleware.csrf import get_token

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
            serializer.save()

            response_data = {
                "message": "User Created Successfully", "data": serializer.data
            }

            return Response(data=response_data, status=200)

        error_data = {"error": serializer.errors}
        return Response(data=error_data, status=400)

@method_decorator(ensure_csrf_cookie, name='dispatch')
class GetCSRFToken(APIView):
    permission_classes = [permissions.AllowAny]
    def get(self, request, *args, **kwargs):
        return Response({"message": "CSRF successfully set!"}, status=200)