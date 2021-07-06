from rest_framework.generics import CreateAPIView, DestroyAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from twitter_api.models import PythonTipSheet, PythonTipUserForm
from .serializers import PythonTipSerializer, PythonTipUserFormSerializer


class GetPythonTipsView(APIView):
    """Retrieves all the python tips in the DB"""
    def get(self, request):
        my_data = PythonTipSheet.objects.all()
        serializer = PythonTipSerializer(my_data, many=True)
        return Response(
            serializer.data
        )


class CreatePythonTipView(CreateAPIView):
    """Python Tip Creation Form"""
    permission_classes = [AllowAny]
    serializer_class = PythonTipUserFormSerializer

    def post(self, request):
        serializer = PythonTipUserFormSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        PythonTipUserForm.objects.create(
            python_tip=serializer.validated_data.get('python_tip'),
            twitter_handle=serializer.validated_data.get('twitter_handle'),
            email=serializer.validated_data.get('email')
        )
        return Response(
            {
                "data": "User created"
            },
            status=status.HTTP_201_CREATED
        )


class EditTipView(APIView):
    """Edits the Python Tip via PATCH"""
    permission_classes = [AllowAny]

    def patch(self, request, id):
        python_tip = PythonTipUserForm.objects.filter(id=id)
        serializer = PythonTipUserFormSerializer(python_tip=python_tip)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            {
                "data": "Edit Successful"
            },
            status=status.HTTP_200_OK
        )


class DeletePythonTip(APIView)
