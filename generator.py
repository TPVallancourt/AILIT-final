import argparse
from collections import defaultdict
from random import choice


def read_cfg(cfg):
    """
    This function takes in a text version of a CFG and returns
    a usable dictionary version of it.
    :param cfg: name of a text file containing a context-free grammar
    :return grammar: a dictionary representing a context-free grammar
    """
    grammar = defaultdict(list)
    with open(cfg, 'r') as f:
        for line in f:
            line = line.split(':')
            lhs = line[0]
            rhs = line[1].rstrip('\n').split(',')
            grammar[lhs].append(rhs)
    return grammar


def make_sentence_from_grammar(grammar_dict):
    """
    This function randomly generates a sentence based on the provided CFG
    :param grammar_dict: a dictionary representing a context-free grammar
    :return output_sentence: a list of words in a sentence
    """
    # start default sentence
    output_sentence = ['S']

    rules_left = True
    while rules_left:

        for index in range(len(output_sentence)):
            # get possible choices from non-terminal
            rhs_choices = grammar_dict[output_sentence[index]]
            if not rhs_choices:
                continue
            # choose random rule
            rhs = choice(rhs_choices)
            # insert result of rule and delete
            # non-terminal that led to rule
            for token in reversed(rhs):
                output_sentence.insert(index, token)
            del output_sentence[index + len(rhs)]

        # check if only words remain in output sentence
        rules_left = False
        for token in output_sentence:
            # words are lowercase, non-terminals are upper
            if token.isupper():
                rules_left = True
                break

    return output_sentence


if __name__ == "__main__":
    # get arguments from command line
    PARSE = argparse.ArgumentParser(description="""
                                    Recreation of Yngve's Random Sentence Generator
                                    """, add_help=True)
    PARSE.add_argument("-c", "--cfg", required=True,
                       help="Text file containing rules of CFG in format RHS:LHS",
                       dest="cfg")
    PARSE.add_argument("-o", "--output", required=False,
                       help="Name for output file",
                       dest="output")
    PARSE.add_argument("-n", "--number", required=False,
                       help="Number of sentences to generate",
                       dest="num")
    ARGS = vars(PARSE.parse_args())

    # give default values if not provided via command line
    outfile = ARGS['output'] if ARGS['output'] else 'output.txt'
    num = ARGS['num'] if ARGS['num'] else 100

    # read the cfg into a dictionary
    grammar_dictionary = read_cfg(ARGS['cfg'])

    # write generated sentences to output file
    with open(outfile, 'w') as o:
        for i in range(num):
            sentence = make_sentence_from_grammar(grammar_dictionary)
            # capitalize first word
            o.write(sentence[0].capitalize() + " ")
            for word in sentence[1:-1]:
                o.write(word + " ")
            # put a period and no space after the word
            o.write(sentence[-1] + ".\n")
