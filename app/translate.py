import json
import requests
from flask_babel import _
from app import app
import os, requests, uuid, json


def translate(text, source_language, dest_language):
    if 'MS_TRANSLATOR_KEY' not in app.config or \
            not app.config['MS_TRANSLATOR_KEY']:
        return _('Error: the translation service is not configured.')
    headers = {'Ocp-Apim-Subscription-Key': app.config['MS_TRANSLATOR_KEY'],
                'Ocp-Apim-Subscription-Region': 'canadacentral',
               'Content-type': 'application/json'}
    url = 'https://api.cognitive.microsofttranslator.com/translate?api-version=3.0&from={}&to={}' \
        .format(source_language, dest_language)
    body = [{'text': text}]
    request = requests.post(url, headers=headers, json=body)
    if request.status_code != 200:
        return 'Error: the translation service failed.'
    return json.loads(request.content.decode('utf-8-sig'))
