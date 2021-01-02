#NLPPython

## environment
conda env create -f nlp_course_env.yml

conda activate nlp_course
conda deactivate nlp_course

jupyter notebook

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
