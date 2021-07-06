from rest_framework.generics import CreateAPIView, DestroyAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import serializers, status
from twitter_api.models import PythonTipSheet, PythonTipUserForm
from .serializers import PythonTipSerializer, PythonTipUserFormSerializer
from drf_yasg.utils import swagger_auto_schema


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

    @swagger_auto_schema(
        request_body=PythonTipUserFormSerializer,
        operation_description="Creates a Tip Object",
        responses={200: 'Done'}
    )
    def post(self, request):
        serializer = PythonTipUserFormSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            {
                "data": "Form Submitted Successfully!"
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


class DeletePythonTip(DestroyAPIView):
    """Deletes any python Tip passed to it"""
    def delete(self, request, *args, **kwargs):
        python_tip = PythonTipUserForm.objects.filter(id=id)
        if python_tip.exists():
            python_tip.delete()
            return Response(
                "Deleted",
                status=status.HTTP_204_NO_CONTENT
            )
