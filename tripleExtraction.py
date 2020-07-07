import re

def argIndexList(predict_result:dict): #引数には文章ごとのpredictor.predict（AllenNLP）の結果の連想配列を与え，{文1:{verb:(arg0,arg1)},文2:{verb:...}}を返す
    triples = {}
    for i,result in predict_result.items():
        triples.setdefault(i,{})
        for verb in result['verbs']:
            ARG0 = [j for j,tag in enumerate(verb['tags']) if re.match('([BI]-)ARG0',tag)]
            ARG1 = [k for k,tag in enumerate(verb['tags']) if re.match('([BI]-)ARG1',tag)]
            if ARG0 != [] and ARG1 != []:
                ARG0 = ' '.join([result['words'][l] for l in ARG0])
                ARG1 = ' '.join([result['words'][m] for m in ARG1])
                triples[i].setdefault(verb['verb'],(ARG0, ARG1))
            else:
                pass
    return triples