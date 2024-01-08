from rest_framework import generics, permissions
from rest_framework.response import Response
from .serializers import SignUpSerializer

class SignUpView(generics.CreateAPIView):
    serializer_class = SignUpSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        # Manually check for validation errors
        if serializer.is_valid():
            serializer.save()

            response_data = {
                "message": "User Created Successfully", "data": serializer.data
            }

            return Response(data=response_data, status=200)

        error_data = {"error": serializer.errors}
        return Response(data=error_data, status=400)
