import pytest
from model_mommy import mommy
from freezegun import freeze_time

from translation.serializers import TranslationSerializer


def test_translation_serializer_from_data_success():
    body = {
        "original_text": "potatoes",
        "translated_text": "molasses",
        "language": "bird"
    }
    expected_data = {
        "original_text": "potatoes",
        "translated_text": "molasses",
        "language": "bird"
    }

    serializer = TranslationSerializer(data=body)

    assert serializer.is_valid() == True
    assert serializer.data == expected_data


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
