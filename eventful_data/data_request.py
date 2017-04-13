import urllib.request
import urllib.parse
import requests
import json

# This includes our secret API key

from secrets import *


def search_venue(self, keyword = None):

    '''
    :param name: name of artist or venue that we are looking for.
    :return: list

    '''
    parameters = urllib.parse.urlencode(({
        'q': keyword
        'l': 'Minnesota',
        'date': 'future',
        "page_size": "200",
        'app_key': EVENTFUL_KEY
    }))


    # response = requests.get('http://api.eventful.com/json/venues/search?', params=parameters).json()

    response = requests.get('http://api.eventful.com/json/events/search?...', params=parameters).json()

    # This will write to the file.
    with open('data.json', 'w', encoding='utf-8') as save_data:
        try:
            json_data = json.dumps(response)
            save_data.write(json_data)
        except Exception as e:
            print('Nothing saved', e)


def main():
    search_venue('concert')

    # search_artist('concert')

if __name__ == "__main__":
    main()
