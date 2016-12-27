from rest_framework import serializers

from app.translation.models import Translation
from app.translation.client import Transltr
from app.translation.errors import TransltrError


class TranslationSerializer(serializers.ModelSerializer):
    """
    Serializer for Translation model
    """

    def validate(self, data):
        """
        Attempts to translate the entered `original_text`. Raises
        ValidationError if there was an error with Transltr.
        """
        original_validation = super(TranslationSerializer, self).validate(data)
        if not original_validation:
            return original_validation 

        transltr = Transltr()
        try:
            translation = transltr.translate_to_en(data['original_text'])
        except TransltrError:
            raise serializers.ValidationError(
                "Unable to translate text, try again later"
            )
        data['translated_text'] = translation.get('translationText')
        data['language'] = translation.get('from')

        return data

    class Meta:
        model = Translation
        fields = ('id', 'original_text', 'translated_text', 'language',
            'timestamp')
        read_only_fields = ('translated_text', 'language', 'timestamp')
