import re

from allennlp.predictors.predictor import Predictor
import allennlp_models.structured_prediction
predictor = Predictor.from_path("https://storage.googleapis.com/allennlp-public-models/openie-model.2020.03.26.tar.gz")

def tripleExtraction(sentence):
    result = predictor.predict(sentence = sentence)
    triples = []
    for verb in result['verbs']:
        ARG0 = [j for j,tag in enumerate(verb['tags']) if re.match('([BI]-)ARG0',tag)]
        ARG1 = [k for k,tag in enumerate(verb['tags']) if re.match('([BI]-)ARG1',tag)]
        if ARG0 != [] and ARG1 != []:
            ARG0 = ' '.join([result['words'][l] for l in ARG0])
            ARG1 = ' '.join([result['words'][m] for m in ARG1])
            triples.append((ARG0, verb['verb'], ARG1))
    return triples