from rest_framework import serializers

from .models import zuriModel

class ZuriSerializer(serializers.ModelSerializer):
    class Meta:
        model = zuriModel
        fields = ('slackUsername', 'backend', 'age', 'bio')