#%%
# https://sobigdata.d4science.org/group/tagme/tagme-help

import requests
import pprint

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

tagme_endpoint = 'https://tagme.d4science.org/tagme/tag'

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

    return json_res

#%%
def confidentAnnotations(json_res, min_rho=default_rho):
    annotations = []
    for entity in json_res['annotations']:
        if entity['rho'] > min_rho:
            annotations.append(entity)
    return annotations