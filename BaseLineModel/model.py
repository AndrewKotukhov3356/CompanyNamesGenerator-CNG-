import random

def generate_the_word(infile):
    random_line = random.choice(open(infile).read().split('\n'))
    return random_line

infile1 = "nouns.txt"
infile2 = "adjf.txt"
sentences = open("sentences.txt", "w") 
i = 0
while i != 100000: 
    print((generate_the_word(infile2) + " " + generate_the_word(infile1)),file = sentences)
    i += 1
