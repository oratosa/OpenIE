import re

import spacy 
nlp = spacy.load("en_core_web_sm")

from allennlp.predictors.predictor import Predictor
import allennlp_models.structured_prediction
predictor = Predictor.from_path("https://storage.googleapis.com/allennlp-public-models/openie-model.2020.03.26.tar.gz")

def tripleExtraction(sentence):
    #tripleの生成
    result = predictor.predict(sentence = sentence)
    triples = []
    for verb in result['verbs']:
        ARG0 = [j for j,tag in enumerate(verb['tags']) if re.match('([BI]-)ARG0',tag)]
        ARG1 = [k for k,tag in enumerate(verb['tags']) if re.match('([BI]-)ARG1',tag)]
        if ARG0 != [] and ARG1 != []:
            ARG0 = ' '.join([result['words'][l] for l in ARG0])
            ARG1 = ' '.join([result['words'][m] for m in ARG1])
            triples.append((ARG0, verb['verb'], ARG1))
        else:
            pass
    return triples

def entityExtraction(sentence):
    #Named entityを抽出する
    doc = nlp(sentence)
    entities = []
    for entity in doc.ents:
        entities.append({entity.text:entity.label_})
    return entities

def NERtripleExtraction(triples, entities):
    NER_triples = []
    for triple in triples:
        s = None
        o = None
        for entity in entities:
            entity = str(entity)
            if entity in triple[0]:
                s = triple[0]
            elif entity in triple[2]:
                o = triple[2]
        if (s is not None) and (o is not None):
            NER_triples.append((s,triple[1],o))
    NER_triples = list(dict.fromkeys(NER_triples))
    if NER_triples != []:
        return NER_triples