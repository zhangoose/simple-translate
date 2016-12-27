import requests

from app.translation.errors import TransltrError


class Transltr(object):
    """
    A client for Transltr.org's API. Documentation here:
    http://www.transltr.org/Developers
    """

    def __init__(self):
        self.BASE_URL = "http://www.transltr.org/api"
    
    def translate_to_en(self, text):
        """
        Takes a string `text` and sending a request to /translate.

        Returns a json representation of the translated text in the form of:
        
        {
            "from": ...,              # detected language of `text`
            "to": "en",               # language to translate to
            "text": ...,              # `text` queried for
            "translationText": .....  # translation of `text`
        }
        """
        body = {
            "text": text,
            "to": "en"
        }
        response = requests.post(self.BASE_URL + "/translate", data=body)

        if response.status_code != 200:
            raise TransltrError()

        return response.json()

