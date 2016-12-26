import pytest
from rest_framework.test import APIClient
from freezegun import freeze_time
from model_mommy import mommy
from pytz import UTC

from datetime import datetime
import json

from app.translation.models import Translation


@pytest.mark.django_db
@freeze_time("2016-01-01 10:10:10")
def test_list_translations():
    translation = mommy.make('translation.Translation')
    client = APIClient()
    expected_data = [
        {
            "id": translation.id,
            "original_text": translation.original_text,
            "translated_text": translation.translated_text,
            "language": translation.language,
            "timestamp": "2016-01-01T10:10:10Z"
        }
    ]

    response = client.get("/translations/", format="json")

    assert response.status_code == 200
    assert response.data == expected_data
    

@pytest.mark.django_db
@freeze_time("2016-01-01 10:10:10")
def test_retrieve_translation():
    translation = mommy.make('translation.Translation')
    client = APIClient()
    expected_data = {
        "id": translation.id,
        "original_text": translation.original_text,
        "translated_text": translation.translated_text,
        "language": translation.language,
        "timestamp": "2016-01-01T10:10:10Z"
    }

    response = client.get("/translations/{}/".format(translation.id),
        format="json")

    assert response.status_code == 200
    assert response.data == expected_data


@pytest.mark.django_db
@freeze_time("2016-01-01 10:10:10")
def test_delete_translation():
    translation = mommy.make('translation.Translation')
    client = APIClient()
    
    response = client.delete("/translations/{}/".format(translation.id))

    assert response.status_code == 204
    assert Translation.objects.count() == 0


@pytest.mark.django_db
@freeze_time("2016-01-01 10:10:10")
def test_create_translation():
    client = APIClient()
    body = {
        "original_text": "potatoes",
        "translated_text": "molasses",
        "language": "bird"
    }

    response = client.post(
        "/translations/",
        json.dumps(body),
        content_type="application/json"
    )

    assert response.status_code == 201
    assert Translation.objects.count() == 1

    translation = Translation.objects.first()

    assert translation.original_text == "potatoes"
    assert translation.translated_text == "molasses"
    assert translation.language == "bird"
    assert translation.timestamp == datetime(2016, 1, 1, 10, 10, 10, tzinfo=UTC)
