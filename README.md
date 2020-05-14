# AILIT-final

Archaeological recreation of Victory Yngve's Random Generation of English Sentences.

## Description of Files

### generator.py
```
usage: generator.py [-h] -c CFG [-o OUTPUT] [-n NUM]

Recreation of Yngve's Random Sentence Generator

optional arguments:
  -h, --help            show this help message and exit
  -c CFG, --cfg CFG     Text file containing rules of CFG in format RHS:LHS
  -o OUTPUT, --output OUTPUT
                        Name for output file
  -n NUM, --number NUM  Number of sentences to generate

```

### bfg_cfg.txt

A text file containing the rules of a context-free grammar. Each line contains a single rule of the CFG.
This CFG was created by taking the first ten sentences in Roald Dahl's The BFG, turning them into parse trees, and writing down the rules necessary to create such trees.

Tokens in capital letters represented non-terminal constituencies. Tokens in lower case letters represent English language words.

Below is a list of all the non-terminal tokens used in this CFG:

* S – Sentence
* NP – Noun phrase
* VP - Verb phrase
* SIM - Simile Phrase
* GP - Gerund Phrase
* PP - Prepositoinal phrase
* ADJ - Adjective
* ADV - Adverb
* DEG - Degree (e.g. quite, very, etc.)
* A - Article
* P - Preposition
* CON - Conjunction
* N - Noun
* PN - Person's name
* PRN - Pronoun
* PSP - Possessive Pronoun
* V - Verb
* AUX - Auxiliary Verb
* G - Gerund
* INF - Infinitive

Two example lines in this CFG are:

S:NP,VP

S:NP,VP,PP

which indicate that a sentence could become either (line 1) a noun phrase followed by a verb phrase or (line 2) a noun phrase, then a verb phrase, then a prepositional phrase.

This would then be represented in a Python dictionary as:

{'S': [['NP', 'VP'], ['NP', 'VP', 'PP']]}

### bfg_output.txt

Example output of generator.py using bfg_cfg.txt 

On each line is a single sentence generated by the program.

This output file contains the default number of 100 sentences.
