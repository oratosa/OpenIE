from nltk import tokenize

def toSentences(message_text):
    sentences = tokenize.sent_tokenize(message_text)
    #sent_tokenizeでは改行コードの除去，文の途中の.への対応ができないため，対処する.
    cleaned = []
    for sentence in sentences:
        cleaned_sentence = ' '.join(sentence.split())
        if cleaned_sentence[0].isupper()==True:
            cleaned.append(cleaned_sentence)
        else:
            cleaned[-1] = cleaned[-1] + ' ' + cleaned_sentence
    return cleaned