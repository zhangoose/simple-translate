import pytest
import mock
from model_mommy import mommy
from freezegun import freeze_time

from app.translation.serializers import TranslationSerializer


@mock.patch("app.translation.serializers.Transltr.translate_to_en")
def test_translation_serializer_from_data_success(mock_transltr):
    mock_transltr.return_value = {
        "from": "es",
        "to": "en",
        "text": "patatas",
        "translationText": "Potatoes"
    }
    body = {
        "original_text": "patatas",
        "translated_text": "Potatoes",
        "language": "es"
    }

    serializer = TranslationSerializer(data=body)

    assert serializer.is_valid() == True
    assert serializer.data == body


def test_translation_serializer_from_data_failure():
    body = {}

    serializer = TranslationSerializer(data=body)

    assert serializer.is_valid() == False


@pytest.mark.django_db
@freeze_time("2016-01-01 10:10:10")
def test_translation_serializer_from_object():
    translation = mommy.make('translation.Translation',
        original_text="potatoes",
        translated_text="molasses",
        language="bird"
    )
    expected_data = {
        "id": translation.id,
        "original_text": "potatoes",
        "translated_text": "molasses",
        "language": "bird",
        "timestamp": "2016-01-01T10:10:10Z"
    }

    serializer = TranslationSerializer(translation)

    assert serializer.data == expected_data
