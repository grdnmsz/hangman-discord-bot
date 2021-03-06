import requests
import os
from dotenv import load_dotenv


load_dotenv()

__headers = {
    'x-rapidapi-key': os.getenv('API_KEY'),
    'x-rapidapi-host': "dicolink.p.rapidapi.com"
}


def get_random_word():
    __query_string = {
        "minlong": "5",
        "maxlong": "-1",
        "verbeconjugue": "false"
    }

    try:
        res = requests.request("GET", os.getenv(
            'WORD_ENDPOINT'), headers=__headers, params=__query_string)
    except:
        raise Exception('Fail to fetch a word, please try again')
        return None 
    else:
        parsed = res.json()[0]
        return parsed["mot"]
