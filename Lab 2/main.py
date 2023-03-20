import matplotlib.pyplot as plt
import networkx as nx
from Automaton import Automaton
from FiniteAutomaton import FiniteAutomaton
from Grammar import Grammars
class Main:
    print('===============================LAB1=====================================')
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
print('')
print('')
print('')
print('=======================================LAB2==========================================')
is_deterministic = automation.is_deterministic()
print(f"Is automaton deterministic? {is_deterministic}")

# Convert NDFA to DFA
dfa = automation.to_dfa()
print(f"DFA states: {dfa.states}")
print(f"DFA transition function: {dfa.transitions}")
print(f"DFA initial state: {dfa.start_state}")
print(f"DFA final states: {dfa.accept_states}")

grammar = automation.to_grammar()
print(f"Regular grammar productions: {grammar}")
print(main.grammar.chomsky_classification())
automation.render()




