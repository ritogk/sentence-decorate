import spacy
from spacy.symbols import obj, VERB, nsubj, iobj, ADJ, AUX, root
import deplacy
import pprint

class Spacy:
    # 文章から述語、目的語、主語を抽出します。
    def sentents_to_doc(self, sentents: str):
        sentents = sentents.split('。')
        nlp = spacy.load('ja_ginza_electra')
        
        # doc = nlp('近年、コンピューターやインターネットの進歩により、誰もが大量の文章へアクセスできるようになってきた。')
        # doc = nlp('春夏連覇を狙う大阪桐蔭が聖望学園に大勝し、春夏連覇を成し遂げた１８年以来４年ぶりに１６強入りを決めた。')

        sentents_analysis = []
        for sent in sentents:
            if(sent == ''): continue
            print(sent)
            element_predicates = []
            element_objects = []
            element_subjects = []
            
            doc = nlp(sent)
            deplacy.render(doc, Japanese=True)
            
            # 述語と名詞だけ抜き出したほうが良いか？まあ一旦これで。
            for tok in doc:
                if tok.dep == obj:
                    element_objects.append(tok.text)
                if tok.dep == nsubj:
                    element_subjects.append(tok.text)
                if tok.dep_ == 'ROOT':
                    element_predicates.append(tok.text)
            sentents_analysis.append({
                'sentent': sent,
                'predicates':element_predicates,
                'objects': element_objects,
                'subjects': element_subjects
            })
        return sentents_analysis
        # https://qiita.com/wf-yamaday/items/3ffdcc15a5878b279d61