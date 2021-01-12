import spacy
nlp = spacy.load('en_core_web_sm')
nlp_es = spacy.load('es_core_news_sm')

print(f'English stop words: {len(nlp.Defaults.stop_words)} words')
print(nlp.Defaults.stop_words)

print(f'\nSpanish stop words: {len(nlp.Defaults.stop_words)} words')
print(nlp_es.Defaults.stop_words)

# can lookup if something is a stop word
is_stop = nlp.vocab['is'].is_stop
print(f"Is 'is' a stop word? {is_stop}")

# add a stop word
nlp.Defaults.stop_words.add('btw')
nlp.vocab['btw'].is_stop = True

print(f'New stop word added: {len(nlp.Defaults.stop_words)} words')
print(f"Is btw a stop word: {nlp.vocab['btw'].is_stop}")

# remove a stop word
nlp.Defaults.stop_words.remove('beyond')
nlp.vocab['beyond'].is_stop = False

