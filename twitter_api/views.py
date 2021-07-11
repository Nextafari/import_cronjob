from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.generics import CreateAPIView, DestroyAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from twitter_api.models import PythonTipSheet, PythonTipUserForm

from .serializers import PythonTipSheetSerializer, PythonTipUserFormSerializer
from allauth.socialaccount.providers.twitter.views import TwitterOAuthAdapter
from rest_auth.registration.views import SocialLoginView
from rest_auth.social_serializers import TwitterLoginSerializer


class TwitterLogin(SocialLoginView):
    serializer_class = TwitterLoginSerializer
    adapter_class = TwitterOAuthAdapter


class GetPythonTipsView(APIView):
    """Retrieves all the python tips in the DB"""
    def get(self, request):
        my_data = PythonTipSheet.objects.all()
        serializer = PythonTipSheetSerializer(my_data, many=True)
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
        python_tip = PythonTipSheet.objects.filter(id=id)
        serializer = PythonTipSheetSerializer(python_tip, data=request.data)
        serializer.is_valid(raise_exception=True)
        PythonTipSheet.objects.filter(id=id).update(
            timestamp=serializer.validated_data.get("timestamp"),
            python_tip=serializer.validated_data.get("python_tip"),
            link=serializer.validated_data.get("link"),
            author=serializer.validated_data.get("author"),
            published="False"
        )
        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )


class DeletePythonTipView(DestroyAPIView):
    """Deletes any python Tip passed to it"""
    def delete(self, request, id, **kwargs):
        python_tip = PythonTipUserForm.objects.filter(id=id)
        if python_tip.exists():
            python_tip.delete()
            return Response(
                "Deleted",
                status=status.HTTP_204_NO_CONTENT
            )
        else:
            return Response("Data object does not Exist")
