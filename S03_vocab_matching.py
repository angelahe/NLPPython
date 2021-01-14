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

# when done with a pattern can now remove the pattern

matcher.remove('SolarPower')

# will find solarpower, SolarPower
pattern4 = [{'LOWER':'solarpower'}]
#allow pattern to match 0 or more times solar*power
pattern5 = [{'LOWER':'solar'},{'IS_PUNCT':True}, {'OP':'*'}, {'LOWER':'power'}]

matcher.add('SolarPower', None, pattern4, pattern5)


doc2 = nlp(u"Solar--Power is solarpower. The Solar Power industry continues to grow a solarpower increases. Solar-power is awesome.")
found_matches2 = matcher(doc2)
print(found_matches2)
