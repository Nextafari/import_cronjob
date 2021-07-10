from rest_framework import serializers

from .models import PythonTipSheet, PythonTipUserForm


class PythonTipSheetSerializer(serializers.ModelSerializer):
    class Meta:
        model = PythonTipSheet
        fields = "__all__"


class PythonTipUserFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = PythonTipUserForm
        fields = [
            "python_tip", "twitter_handle", "email",
        ]

    def validate(self, attrs):
        python_tip = attrs["python_tip"]
        if PythonTipUserForm.objects.filter(python_tip=python_tip).exists():
            raise serializers.ValidationError({
                'python_tip': 'This tip already exits'
                })
        return super().validate(attrs)
