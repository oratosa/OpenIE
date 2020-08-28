#%%
# https://sobigdata.d4science.org/group/tagme/tagme-help
# https://www.mediawiki.org/wiki/API:Query/ja

import requests
import pprint

#Parameters on tagme
with open('gcube-token.tagme') as f:
    GCUBE_TOKEN = f.readline()

default_lang='en'
default_tweet='false'
default_include_abstract='false'
default_include_categories='true'
default_include_all_spots='false'
default_long_text=3,
default_epsilon=0.3

default_rho=0.1

tagme_endpoint='https://tagme.d4science.org/tagme/tag'

#Parameters on mediawiki
mediawiki_endpoint='https://en.wikipedia.org/w/api.php'
default_action='query'
default_format='json'
default_prop='info'
default_inprop='url'

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
    response = requests.post(tagme_endpoint, params=params)
    json_res = response.json()

    return json_res #jsonを辞書形式にした結果

#%%
def confidentAnnotations(json_res, min_rho=default_rho):
    annotations = []
    for entity in json_res['annotations']:
        if entity['rho'] > min_rho:
            annotations.append(entity)
    return annotations #annotationsキーのバリューとなるentityのリスト

#%%
def mediaWiki(pageid, action=default_action, format=default_format, prop=default_prop, inprop=default_inprop):
    params = {'action':default_action,
            'format':format,
            'prop':default_prop,
            'inprop':default_inprop,
            'pageids':pageid}
    response = requests.get(mediawiki_endpoint, params=params)
    json_res = response.json()
    return json_res
# %%
