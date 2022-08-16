from service.spacy_service import SpacyService
spacy_service = SpacyService()

result = spacy_service.sentents_to_doc('彼女は図書館で本をたくさん読む。')
print(result)