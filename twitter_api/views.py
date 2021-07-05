from django.shortcuts import render
from rest_framework.views import APIView
from .tasks import say_hello
from rest_framework.response import Response


class TestViee(APIView):
    def get(self, request):
        say_hello.delay()
        return Response("Done!")


