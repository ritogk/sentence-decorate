from typing import List
import spacy
from spacy.symbols import obj, VERB, nsubj, iobj, ADJ, AUX, root
import deplacy
from typing_extensions import TypedDict

class SententAnalysis(TypedDict):
  sentent: str
  predicates: list[str]
  objects: list[str]
  subjects: list[str]

class SpacyService:
    # 文章から述語、目的語、主語を抽出します。
    def sentents_to_doc(self, sentents: str) -> list[SententAnalysis]:
        # 抽出結果
        sentents_analyses: list[SententAnalysis] = []
        # モデルロード
        nlp = spacy.load('ja_ginza_electra')
        # 文章を文単位に整形
        sentents = sentents.split('。')
        for sent in sentents:
            if(sent == ''): continue
            
            element_predicates = []
            element_objects = []
            element_subjects = []

            doc = nlp(sent)
            # 構文解析の結果を出力
            deplacy.render(doc, Japanese=True)

            for tok in doc:
                # 目的語を抽出
                if tok.dep == obj:
                    element_objects.append(tok.text)
                # 主語を抽出
                if tok.dep == nsubj:
                    element_subjects.append(tok.text)
                # 述語?を抽出
                if tok.dep_ == 'ROOT':
                    element_predicates.append(tok.text)
            sentents_analyses.append({
                'sentent': sent,
                'predicates':element_predicates,
                'objects': element_objects,
                'subjects': element_subjects
            })
        return sentents_analyses