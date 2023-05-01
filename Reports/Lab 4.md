# Chomsky Normal Form

**Course:** Formal Languages & Finite Automata  
**Author:** Sirghi Tudor \
**Variant:** 28

## Grammar


G=(VN, VI, P, S) Vn={S, A, B, C, D, X} VT={a, b}
P={ 
1. S → B
2. A → aX
3. A → bX
4. X → empty
5. X → BX
6. X → b
7. B → AXaD
8. D → aD
9. D → a
10. C → Ca 
## Theory

Chomsky Normal Form (CNF) is a simplified form of context-free grammars that is useful in both the study and the development of algorithms for parsing and other language-processing tasks. A context-free grammar is said to be in Chomsky Normal Form if all its production rules are in one of the following two forms:

1. A -> BC, where A, B, and C are non-terminal symbols.
2. A -> a, where A is a non-terminal symbol, and a is a terminal symbol. 

The main advantage of CNF is its simplicity, which makes it easier to develop algorithms that work with context-free grammars. Any context-free grammar can be converted into an equivalent grammar in Chomsky Normal Form. The conversion process involves the following steps:

1. Eliminate ε-productions: Replace any production rule of the form A -> ε with alternative productions that generate the same language without the ε-production.
2. Eliminate renaming (unit productions): Remove production rules of the form A -> B, where A and B are non-terminal symbols, and substitute the production rules for B in place of A.
3. Eliminate inaccessible symbols: Remove any non-terminal symbols that cannot be reached from the start symbol in the grammar.
4. Eliminate non-productive symbols: Remove any non-terminal symbols that cannot derive any terminal strings.
5. Convert remaining rules to CNF: Break down production rules with more than two symbols on the right-hand side into multiple rules that conform to the CNF format.

By following these steps, we can transform any context-free grammar into an equivalent grammar in Chomsky Normal Form without altering the language it generates.

## Objectives

1. Implement a method for normalizing an input grammar by the rules of CNF (Chomsky Normal Form).
2. Encapsulate the implementation in a method with an appropriate signature (also ideally in an appropriate class/type).
3. Execute and test the implemented functionality.
4. (Bonus) Create unit tests that validate the functionality of the project.
5. (Bonus) Make the function accept any grammar, not only the one from the student's variant.

## Implementation description

### Eliminate Epsilon Productions

The `eliminate_epsilon` method is responsible for removing ε-productions (rules of the form A -> ε) from the grammar. It identifies all non-terminal symbols that generate ε directly or indirectly and substitutes them in all other production rules, effectively removing the need for ε-productions.


### Eliminate Renaming
The `eliminate_renaming` method removes unit productions (rules of the form A -> B, where A and B are non-terminal symbols) from the grammar. It does so by replacing the unit production with all the production rules of the referenced non-terminal symbol. This process is repeated until all unit productions are eliminated.


### Eliminate Inaccessible Symbols

The `eliminateInaccessibleSymbols` part of the `eliminate_renaming` removes non-terminal symbols that are not reachable from the start symbol of the grammar. It starts with the start symbol and iteratively finds all non-terminal symbols reachable from it. Then, it removes any production rules containing non-reachable symbols.



### Eliminate Non-Productive Symbols

The `eliminate_nonproductive` method removes non-terminal symbols that cannot derive any terminal strings. It first identifies all non-productive symbols and then removes any production rules containing them. This step ensures that every non-terminal symbol in the grammar can derive at least one terminal string.



### Convert to Chomsky Normal Form
The `chomsky_normal_form` method converts the remaining production rules to the CNF format. It does so by breaking down rules with more than two symbols on the right-hand side into multiple rules that conform to CNF. Additionally, it introduces new non-terminal symbols for terminal symbols within rules containing more than one symbol on the right-hand side.


These methods, when executed in sequence, transform the input grammar into an equivalent grammar in Chomsky Normal Form.



# Conclusions
In conclusion, using Chomsky Normal Form (CNF) to represent a grammar has several advantages. CNF grammars are easier to analyze and manipulate, which can simplify the process of generating and parsing sentences. 
Additionally, the restrictions imposed by CNF can lead to more efficient parsing algorithms. 
However, converting a grammar to CNF can be a non-trivial task, and some grammars may not be able to be converted to CNF at all. 
Overall, using CNF can be a useful tool in the study of formal languages and can provide insights into the structure of natural languages.
