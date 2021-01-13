# id and label phrases

import spacy
nlp = spacy.load('en_core_web_sm')

from spacy.matcher import Matcher

matcher = Matcher(nlp.vocab)

# SolarPower
# Solar-power
# Solar power
pattern1  = [{'LOWER':'solarpower'}]
pattern2 = [{'LOWER':'solar'},{'IS_PUNCT':True},{'LOWER':'power'}]
pattern3 = [{'LOWER':'solar'},{'LOWER':'power'}]

matcher.add('SolarPower',None,pattern1,pattern2,pattern3)
doc = nlp(u"The Solar Power industry continues to grow a solarpower increases. Solar-power is awesome.")
found_matches = matcher(doc)

#returns matchid, start token, stop token
print(found_matches)
print('\n')
for match_id, start, end in found_matches:
    string_id = nlp.vocab.strings[match_id]
    span = doc[start:end]
    print(match_id, string_id, start, end, span.text)