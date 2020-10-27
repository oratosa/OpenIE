#%%
# https://sobigdata.d4science.org/group/tagme/tagme-help
# https://www.mediawiki.org/wiki/API:Query/ja

import requests
import pprint
import json

#Parameters on tagme
with open('gcube-token.tagme') as f:
    GCUBE_TOKEN = f.readline()

default_lang='en'
default_tweet='false'
default_include_abstract='false'
default_include_categories='false'
default_include_all_spots='false'
default_long_text=10,
default_epsilon=0.3

default_rho=0.1

tagme_endpoint='https://tagme.d4science.org/tagme/tag'

#Parameters on mediawiki
mediawiki_endpoint='https://en.wikipedia.org/w/api.php'
default_action='query'
default_format='json'
default_prop='pageprops'

#%%
def tagme(text, GCUBE_TOKEN=GCUBE_TOKEN, lang=default_lang, tweet=default_tweet, include_abstract=default_include_abstract,
        include_categories=default_include_categories, include_all_spots=default_include_all_spots, long_text=default_long_text,
        epsilon=default_epsilon):
    params = {'text':text,
        'gcube-token':GCUBE_TOKEN,
        'lang':lang,
        'tweet':tweet,
        'include_abstract':include_abstract,
        'include_categories':include_categories,
        'include_all_spots':include_all_spots,
        'long_text':long_text,
        'epsilon':epsilon
        }
    try:
        response = requests.post(tagme_endpoint, params=params)
        json_res = response.json()
        return json_res #jsonを辞書形式にした結果
    except json.JSONDecodeError:
        return None

#%%
def getWikidataID(pageid):
    params = {'action':default_action,
            'format':default_format,
            'prop':default_prop,
            'pageids':pageid}
    try:
        response = requests.get(mediawiki_endpoint, params=params)
        json_res = response.json()
        return json_res
    except json.JSONDecodeError:
        return None
# %%
