# Laboratory 2 Report

### Course: Formal Languages & Finite Automata

### Author: Sirghi Tudor

## Theory

The main concepts used in that laboratory work are:

- Grammar: A grammar is a set of rules for generating strings in a language. In computer science, grammars are often used to describe the syntax of programming languages or other formal languages. A grammar consists of a set of production rules that specify how to form valid strings in the language.
- Finite state automaton: A finite state automaton (FSA) is a mathematical model of computation that can be used to recognize or generate strings in a language. An FSA consists of a finite number of states, which can transition between each other based on input symbols.
- Non-Deterministic Finite Automaton: NFA is a type of FSA where multiple transitions can be made from a single state on the same input symbol.
- Deterministic Finite Automaton: DFA is a type of FSA where there is only one transition from each state on a given distinct input symbol.
<ul> 
<li>Chomsky Classification: Chomsky hierarchy is a way of classifying formal languages based on the type of grammar that generates them. The hierarchy consists of four levels:</li>
<ul>
<li>Type 0: Unrestricted grammars</li>
<li>Type 1: Context-sensitive grammars</li>
<li>Type 2: Context-free grammars</li>
<li>Type 3: Regular grammars</li>
</ul>
</ul>

##  Objectives
1. Understand what an automaton is and what it can be used for.
2. Continuing the work in the same repository and the same project, the following need to be added:
   a. Provide a function in your grammar type/class that could classify the grammar based on Chomsky hierarchy.
   b. For this you can use the variant from the previous lab.
3. According to your variant number (28), get the finite automaton definition and do the following tasks:
   a. Implement conversion of a finite automaton to a regular grammar.
   b. Determine whether your FA is deterministic or non-deterministic.
   c. Implement some functionality that would convert an NDFA to a DFA.
   
## Implementation
In order to show the execution you can implement a client class/type, which is just a ”Main” class/type
in which you can instantiate the types/classes. Another approach would be to write unit tests if you
are familiar with them.

### Code

```python

import matplotlib.pyplot as plt
import networkx as nx
from Automaton import Automaton
from FiniteAutomaton import FiniteAutomaton
from Grammar import Grammars
class Main:
    def __init__(self):
        self.productions = {
            'S': ['aA'],
            'A': ['aB', 'bS'],
            'B': ['aB','bC'],
            'C': ['aA', 'b'],
        }
        self.start_symbol = 'S'
        self.grammar = Grammars(self.productions, self.start_symbol)
        self.finite_automaton = self.grammar.to_finite_automaton()
        self.automaton = FiniteAutomaton

    def generate_strings(self, num_strings):
        for i in range(num_strings):
            string = self.grammar.generate_string()
            print(string)

if __name__ == '__main__':
    main = Main()
    main.generate_strings(5)
    automatons = main.grammar.to_finite_automaton()
    automaton = {
         'states': {'q0', 'q1', 'q2', 'q3', 'q4'},
    'alphabet': {'a', 'b'},
    'transition': {
        'q0': {'a': 'q1'},
        'q1': {'a': 'q1', 'b': 'q2'},
        'q2': {'a': 'q3', 'b': 'q4'},
        'q3': {'a': 'q1', 'b': 'q2'},
        'q4': {'a': 'q3', 'b': 'q4'},
    },
    'start_state': 'q0',
    'final_states': {'q1', 'q2', 'q3', 'q4'}
    }
    
    checker = FiniteAutomaton(automaton)
    checker.check_strings(['aab', 'abcbb', 'bac', 'cab', 'ccaabb'])
    print(automatons)
    
automation = Automaton()
automation.states = ['q0', 'q1', 'q2', 'q3']
automation.alphabet = ['a', 'b', 'c']
automation.transitions = {('q0', 'a'): ['q0', 'q1'],
                        ('q0', 'b'): ['q2'],
                        ('q1', 'a'): ['q1'],
                        ('q1', 'c'): ['q2'],
                        ('q1', 'b'): ['q3'],
                        ('q2', 'c'): ['q0'],
                        ('q2', 'b'): ['q3']}
automation.start_state = 'q0'
automation.accept_states = ['q3']
is_deterministic = automation.is_deterministic()
print(f"Is automaton deterministic? {is_deterministic}")

# Convert NDFA to DFA
dfa = automation.to_dfa()
print(f"DFA states: {dfa.states}")
print(f"DFA transition function: {dfa.transitions}")
print(f"DFA initial state: {dfa.start_state}")
print(f"DFA final states: {dfa.accept_states}")
```

## Conclusion
In conclusion, formal languages and finite automata are important concepts in computer science that have significant implications for various fields such as artificial intelligence, natural language processing, and computational linguistics. 
Understanding the fundamental concepts of formal languages and finite automata, including determinism, conversion from NFAs to DFAs, and the Chomsky hierarchy, is crucial for designing efficient algorithms and developing powerful computational models. 
With their ability to recognize and generate languages, formal languages and finite automata provide a theoretical foundation for designing efficient and reliable computer systems, making them vital to the advancement of modern technology.
