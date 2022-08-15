from service.spacy import Spacy
spacy = Spacy()

result = spacy.sentents_to_doc('彼女は図書館で本をたくさん読む。')
print(result)

# https://note.com/npaka/n/n5c3e4ca67956