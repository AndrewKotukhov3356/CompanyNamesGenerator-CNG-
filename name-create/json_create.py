#Please import needed libraries below!

from rusyll import rusyll
from markovify import Chain
from enum import Enum, unique

import markovify
import json

# Json creator function:


def main(input_file, output_file):
    corpus = []
    lines_processed = 0

    for line in input_file:
        lines_processed += 1
        try:
            corpus.append(
                rusyll.word_to_syllables_safe_wd(
                    line.strip().lower()))
        except AssertionError:
            pass

    chain = Chain(corpus, 1)
    with open(output_file, 'w+') as f:
        f.write(chain.to_json())

# Empty txt file creator function:

def create_empty_txt(txtfile, mode):
    with open(txtfile, mode) as jell:
        jell = open(txtfile, mode)
    return jell

# Class of types we will use:

class WordTypes(Enum):
    NOUN = "Существительное"
    ADJECTIVE = "Прилагательное"

# Main class to create magic words:

class WordMaker:
    def __init__(self, json_file) -> None:  # Markov chain function.
        self.chains = {}
        for wtype in WordTypes:
            self.chains[wtype] = markovify.Chain.from_json(json_file)

    # Producing words from created markov chain.
    def make_a_word(
            self,
            word_type: WordTypes,
            attempts: int = 100) -> str:
        for _ in range(attempts):
            word = "".join(self.chains[word_type].walk())
            if len(word) > 3:
                return word
        raise ValueError("Error!!!")

