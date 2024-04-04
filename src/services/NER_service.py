import spacy
nlp = spacy.load('en_core_web_lg')

def ner_spacy(text):
    if not text or type(text) is not str:
        return {"error": "Invalid input"}
    doc = nlp(text)
    entities = {}
    i= 0 
    for ent in doc.ents:
        entities[i] = {'text': ent.text, 'label': ent.label_, 'start_char': ent.start_char, 'end_char': ent.end_char}
        i +=1
    return entities

if __name__ == "__main__":
    text = "Microsoft Corporation is located in Redmond, Washington."
    print(ner_spacy(text))