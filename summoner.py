__author__ = 'filipe'

import settings
import requests
import json
import os


class Summoner(object):
    def __init__(self, name=settings.SUMMONER_NAME):
        self.name = name
        self.db = ''
        self.data = ''
        self.path = os.path.dirname(__file__)
        self.cache_dir = settings.CACHE_DIR

    def grab_profile(self):
        # sample https://REGINAL_ENDPOINT['BR']/api/lol/br/v1.4/summoner/by-name/RiotSchmick?api_key=API_KEY
        url = 'https://{0}/api/lol/{1}/v1.4/summoner/by-name/{2}?api_key={3}'.format(settings.REGINAL_ENDPOINT[settings.DEFAULT_REGION.upper()], settings.DEFAULT_REGION, settings.SUMMONER_NAME, settings.API_KEY)
        r = requests.get(url)
        self.persist_json('profile', r.json())
        return r.json()

    def grab_masteries(self, summoner_id):
        # GET /api/lol/{region}/v1.4/summoner/{summonerIds}/masteries
        url = 'https://{0}/api/lol/{1}/v1.4/summoner/{2}/masteries?api_key={3}'.format(settings.REGINAL_ENDPOINT[settings.DEFAULT_REGION.upper()], settings.DEFAULT_REGION, summoner_id, settings.API_KEY)
        r = requests.get(url)
        self.persist_json('masteries', r.json())
        return r.json()

    def grab_runes(self, summoner_id):
        # GET /api/lol/{region}/v1.4/summoner/{summonerIds}/runes
        url = 'https://{0}/api/lol/{1}/v1.4/summoner/{2}/runes?api_key={3}'.format(settings.REGINAL_ENDPOINT[settings.DEFAULT_REGION.upper()], settings.DEFAULT_REGION, summoner_id, settings.API_KEY)
        r = requests.get(url)
        self.persist_json('runes', r.json())
        return r.json()

    def grab_recent_games(self, summoner_id):
        # GET /api/lol/{region}/v1.3/game/by-summoner/{summonerId}/recent
        url = 'https://{0}/api/lol/{1}/v1.3/game/by-summoner/{2}/recent?api_key={3}'.format(settings.REGINAL_ENDPOINT[settings.DEFAULT_REGION.upper()], settings.DEFAULT_REGION, summoner_id, settings.API_KEY)
        r = requests.get(url)
        self.persist_json('recent_games', r.json())
        return r.json()

    def persist_json(self, db, data):
        self.db = db
        self.data = data
        cache = '.'.join([self.db, 'json'])
        cache = os.path.join(self.path, self.cache_dir, cache)
        if not os.path.exists(cache):
            with open(cache, 'a+') as fp:
                json.dump(self.data, fp)

    def search_json(self, db, data):
        pass