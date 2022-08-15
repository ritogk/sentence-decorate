import spacy
from spacy.symbols import obj, VERB, nsubj, iobj, ADJ, AUX, root
import deplacy

class Spacy:
    # 文章から述語、目的語、主語を抽出します。
    def sentents_to_doc(self, sentents: str):
        sentents = sentents.split('。')
        nlp = spacy.load('ja_ginza_electra')

        sentents_analysis = []
        for sent in sentents:
            if(sent == ''): continue
            print(sent)

            element_predicates = []
            element_objects = []
            element_subjects = []
            
            doc = nlp(sent)
            deplacy.render(doc, Japanese=True)

            for tok in doc:
                # 目的語
                if tok.dep == obj:
                    element_objects.append(tok.text)
                # 主語
                if tok.dep == nsubj:
                    element_subjects.append(tok.text)
                # 述語?
                if tok.dep_ == 'ROOT':
                    element_predicates.append(tok.text)
            sentents_analysis.append({
                'sentent': sent,
                'predicates':element_predicates,
                'objects': element_objects,
                'subjects': element_subjects
            })
        return sentents_analysis