import requests as req
import os
from dotenv import load_dotenv


load_dotenv()

_headers = {
    'x-rapidapi-key': os.getenv('API_KEY'),
    'x-rapidapi-host': "dicolink.p.rapidapi.com"
}


def get_random_word() -> None or str:
    _query_string = {
        "minlong": "5",
        "maxlong": "-1",
        "verbeconjugue": "false"
    }

    try:
        res = req.request("GET", os.getenv(
            'WORD_ENDPOINT'), headers=_headers, params=_query_string)
    except:
        raise Exception('Fail to fetch a word, please try again')
        return None
    else:
        parsed_response = res.json()[0]
        return parsed_response["mot"]


def get_word_definition(word: str) -> str:
    """Return the last definition - considered 
    the least obvious - of the word
    if there is more than one
    """
    if type(word) is not str or not len(word):
        return ''

    DEF_ENDPOINT = os.getenv('DEF_ENDPOINT')
    try:
        res = req.request("GET", DEF_ENDPOINT.format(word), headers=_headers)
    except:
        raise Exception('Fail to fetch definition')
        return ''
    else:  # Take the last definition , format, return
        parsed_response = res.json()[-1]
        definition, source = parsed_response["definition"], parsed_response["source"]
        res = '{0}, définition: {1} (source : {2})'.format(
            word, definition, source)
        return res
