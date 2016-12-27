import pytest
from rest_framework.test import APIClient
from freezegun import freeze_time
from model_mommy import mommy
from pytz import UTC
import httpretty

from datetime import datetime
import json

from app.translation.models import Translation


@pytest.mark.django_db
@freeze_time("2016-01-01 10:10:10")
def test_list_translations(api_client):
    translation = mommy.make('translation.Translation')
    expected_data = [
        {
            "id": translation.id,
            "original_text": translation.original_text,
            "translated_text": translation.translated_text,
            "language": translation.language,
            "timestamp": "2016-01-01T10:10:10Z"
        }
    ]

    response = api_client.get("/api/translations/", format="json")

    assert response.status_code == 200
    assert response.data == expected_data
    

@pytest.mark.django_db
@freeze_time("2016-01-01 10:10:10")
def test_retrieve_translation(api_client):
    translation = mommy.make('translation.Translation')
    expected_data = {
        "id": translation.id,
        "original_text": translation.original_text,
        "translated_text": translation.translated_text,
        "language": translation.language,
        "timestamp": "2016-01-01T10:10:10Z"
    }

    response = api_client.get("/api/translations/{}/".format(translation.id),
        format="json")

    assert response.status_code == 200
    assert response.data == expected_data


@pytest.mark.django_db
@freeze_time("2016-01-01 10:10:10")
def test_delete_translation(api_client):
    translation = mommy.make('translation.Translation')
    
    response = api_client.delete(
        "/api/translations/{}/".format(translation.id)
    )

    assert response.status_code == 204
    assert Translation.objects.count() == 0


@pytest.mark.django_db
@freeze_time("2016-01-01 10:10:10")
@httpretty.activate
def test_create_translation():
    client = APIClient()
    body = {
        "original_text": "patatas",
    }
    transltr_body = r"""
    {
        "from": "es",
        "to": "en",
        "text": "patatas",
        "translationText": "Potatoes"
    }
    """
    httpretty.register_uri(
        httpretty.POST,
        "http://www.transltr.org/api/translate",
        body=transltr_body,
        content_type="application/json"
    )
    expected_data = {
        "original_text": "patatas",
        "language": "es",
        "translated_text": "Potatoes",
        "timestamp": "2016-01-01T10:10:10Z"
    }

    response = client.post(
        "/api/translations/",
        json.dumps(body),
        content_type="application/json"
    )

    assert response.status_code == 201

    assert response.data['original_text'] == "patatas"
    assert response.data['language'] == "es"
    assert response.data['translated_text'] == "Potatoes"
    assert response.data['timestamp'] == "2016-01-01T10:10:10Z"

    assert Translation.objects.count() == 1

    translation = Translation.objects.first()

    assert translation.original_text == "patatas"
    assert translation.translated_text == "Potatoes"
    assert translation.language == "es"
    assert translation.timestamp == datetime(2016, 1, 1, 10, 10, 10, tzinfo=UTC)


@pytest.mark.django_db
@httpretty.activate
def test_create_translation_failure():
    client = APIClient()
    body = {
        "original_text": "i want this to fail"
    }
    httpretty.register_uri(
        httpretty.POST,
        "http://www.transltr.org/api/translate",
        body="Some error message",
        status=500,
        content_type="application/json"
    )

    response = client.post(
        "/api/translations/",
        json.dumps(body),
        content_type="application/json"
    )

    assert response.status_code == 400
    assert response.data == {
        "non_field_errors": ["Unable to translate text, try again later"]
    }

    assert Translation.objects.count() == 0

