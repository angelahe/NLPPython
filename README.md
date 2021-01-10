#NLPPython

## environment
conda env create -f nlp_course_env.yml

conda activate nlp_course
conda deactivate nlp_course

jupyter notebook

## installing libraries
conda install -c conda-forge spacy
python -m spacy download en
python -m spacy download es_core_news_sm

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