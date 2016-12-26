from rest_framework import serializers
from app.translation.models import Translation


class TranslationSerializer(serializers.ModelSerializer):
    """
    Serializer for Translation model
    """
    timestamp = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Translation
        fields = ('id', 'original_text', 'translated_text', 'language',
            'timestamp')
