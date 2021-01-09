#vim 
## vim reminders
https://vim.rtorr.com/
move: eg 4 j go down 4 lines
h j k l
H M L
w e b
W E B
0 - start of line
^ - 1st non blank char
gg - 1st line of doc
G - last line
5G - line 5
{ } - jump to next/prev paragraph
move screens: down 1, up 1, up 1 screen, down 1 screen, 1/2 screen
Ctrl+e y b f d u

insert:
r - replace character
i - before cursor
I - at beginning of line
a - after cursor
A - end of line
o - append new line below current
O - append above current line

cut/paste:
yy - copy line (2yy for 2 lines)
y$ - copy to end of line
p - paste
dd - delete 1 line, 2dd
dw - delete word
D - delete to end of line
d$ cut to end of line
x - delete
> shift text right
< shift text left

## git learnings
git reset filename.txt  #to unstage a git add

# parseSqlToClauses.py

takes a 3 column csv file with english, sql, raw text 
outputs to specified csv with original input plus columns for select, from, where, group, order clauses
outputs parseErrors.csv
```bash
 python src/parseSqlToClauses.py tests/testsqlparse.csv tests/testsqlparse_parsed.csv

```

## further reading
https://www.digitalocean.com/community/tutorials/how-to-index-and-slice-strings-in-python-3
https://towardsdatascience.com/a-brief-introduction-to-intent-classification-96fda6b1f557
https://en.wikipedia.org/wiki/Natural-language_understanding
https://en.wikipedia.org/wiki/Deep_learning
https://github.com/Dark-Sied/Intent_Classification
https://en.wikipedia.org/wiki/Gated_recurrent_unit
http://tcci.ccf.org.cn/conference/2017/papers/1158.pdf
https://textminingonline.com/dive-into-nltk-part-iv-stemming-and-lemmatization
https://en.wikipedia.org/wiki/WordNet