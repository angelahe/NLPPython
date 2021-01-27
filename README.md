#NLPPython

## environment
conda env create -f nlp_course_env.yml
conda env create -f nlp_course2_env.yml

conda activate nlp_course
conda deactivate nlp_course

jupyter notebook

## installing libraries
conda install -c conda-forge spacy
python -m spacy download en
python -m spacy download es_core_news_sm
python -m spacy download en_core_web_sm

python -m spacy download en_core_web_md
python -m spacy download en_core_web_lg

conda install scikit-learn
pip install scikit-learn

can load en_core_web_lg for a larger corpus

## specific to jupyter
shift + enter to end the line
%%writefile test.txt
Hello, this is a quick test file.
this is the second line of the file.

myfile = open('test.txt')
myfile = open("/Users/angela/kata/2021code/xxx.txt")
myfile.read()

shift + tab (for arguments of a function)

## working with text files
see strftime.org for datetime formats

## working with pdfs
PyPDF2 library

## additional reading
https://spacy.io/api/annotation#pos-tagging
https://spacy.io/api/annotation#dependency-parsing
languages supported i could see:
english, german, spanish, portuguese, french, italian, dutch
https://spacy.io/api/annotation#dependency-parsing
https://spacy.io/usage/visualizers
https://spacy.io/api/top-level#displacy.options
https://spacy.io/usage/models

## notes
tag:
.text - original word text
.lemma_ - base form of the word
.pos_ - part of speed tag
.tag_ detailed part of speech tag
.shape_ word shape with capitalization, puctuation, digits
.is_alpha - is the token an alpha character
.is_stop - is the token part of a stop list ie the most common words of the language

use span (slice of a doc object)

OP key:
\! negate the pattern, require it to match 0 times
? make the pattern optional
\+ require pattern to match 1 or more times
\* allow pattern to match 0 or more times

other token attributes
'ORTH' exact verbatim text of token
'LOWER' lowercase form of token text
'LENGTH' length of token text
'IS_ALPHA', 'IS_ASCII', 'IS_DIGIT'
'IS_LOWER', 'IS_UPPER', 'IS_TITLE'
'IS_PUNCT', 'IS_SPACE', 'IS_STOP'
'LIKE_NUM', 'LIKE_URL', 'LIKE_EMAIL'
'POS', 'TAG', 'DEP', 'LEMMA', 'SHAPE'   tokens simple and extended part of speech tag, dependency label, lemma, shape
'ENT_TYPE' token entity label