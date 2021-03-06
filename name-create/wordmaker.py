# -*- coding: utf-8 -*-
"""WordMaker
"""

import json
import json_create

# Opening our TF-IDF sorted files:

# NOUNS:
n = open('nouns.txt', 'r').readlines()

# ADJECTIVES:
a = open('adjf.txt', 'r').readlines()

# Creating json files for each txt file using our main function:

# NOUNS:
json_create.main(n, 'nouns.json')

# ADJECTIVES:
json_create.main(a, 'adjf.json')

# Opening json files:
f = open('nouns.json')
h = open('adjf.json')
json_file1 = json.load(f)
json_file2 = json.load(h)

k = 0
while k != 10:
 emp = json_create.WordMaker(json_file1)
 c = emp.make_a_word(json_create.WordTypes.NOUN, 500)
 if c in n:
     c = c.replace(c, " ")
 emp = json_create.WordMaker(json_file2)
 b = emp.make_a_word(json_create.WordTypes.ADJECTIVE, 500)
 if b in n:
     b = b.replace(b, " ")
 print(b + " " + c)
 k += 1
