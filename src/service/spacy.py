import spacy
from spacy.symbols import obj, VERB, nsubj, iobj
import deplacy

class Spacy:
    # htmlをspacy形式のdocに変換を行います。
    def html_to_doc(self, html: str):
        nlp = spacy.load('ja_ginza_electra')

        # doc = nlp('近年、コンピューターやインターネットの進歩により、誰もが大量の文章へアクセスできるようになってきた。')
        doc = nlp('春夏連覇を狙う大阪桐蔭が聖望学園に大勝し、春夏連覇を成し遂げた１８年以来４年ぶりに１６強入りを決めた。')
        deplacy.render(doc, Japanese=True)

        for tok in doc:
            # print('目的語；' + tok.text)
            # if tok.dep == obj:
            #   print('目的語；' + tok.text)
            # if tok.dep == VERB:
            #   print('動詞：' + tok.text)
            if tok.dep == nsubj:
                print('主語:' + tok.text)
            if tok.dep == iobj:
                print('熟語:' + tok.text)

        return html