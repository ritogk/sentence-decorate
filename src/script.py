from service.spacy import Spacy
spacy = Spacy()

result = spacy.sentents_to_doc('高市氏は10日の内閣改造・党役員人事で自民党政調会長を辞し、経済安保担当相に就任。10日の記者会見で世界平和統一家庭連合（旧統一教会）関連の「世界日報」が発行する月刊誌に対談が掲載されていたことを認めた。さらに12日、同日午後に予定していた小林前担当相らからの引き継ぎ式を中止し、内閣府職員へのあいさつ式を欠席した。')
print(result)

# https://note.com/npaka/n/n5c3e4ca67956