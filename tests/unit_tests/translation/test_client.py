import pytest
import httpretty

import json

from app.translation.client import Transltr
from app.translation.errors import TransltrError


@httpretty.activate
def test_translate_to_en_success():
    client = Transltr()
    body = r"""
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
        body=body,
        content_type="application/json"
    )
    expected_result = {
        "from": "es",
        "to": "en",
        "text": "patatas",
        "translationText": "Potatoes"
    }

    actual = client.translate_to_en("potatoes")

    assert actual == expected_result


@httpretty.activate
def test_translate_to_en_failure():
    client = Transltr()
    httpretty.register_uri(
        httpretty.POST,
        "http://www.transltr.org/api/translate",
        body="Some error message",
        status=500,
        content_type="application/json"
    )
    
    with pytest.raises(TransltrError):
        client.translate_to_en("potatoes")

