# Requirements Specification

---

The text generator aims to generate natural language using Markov chains contained in a Trie data structure.

## Language

The primary programming language used is Python. Other proficient languages include JavaScript. 

## Algorithms and Data Structures

The program primarily relies on a stochastic model called the Markov chain. The model describes a sequence of possible events, where every event in that sequence only depends on the predetermined number of previous events. The term 'degree' is a standard way to referer to the number of prior events taken into account.

The program utilizes a Trie data structure to store the Markov chain. In our case, the Trie data structure, sometimes referred to as a prefix tree, stores n + 1-word sequences, where n is the degree. To illustrate further, take an example text, "The dog ate the bone and drank water." To create a second-degree Markov chain, we'd store the following sequences to the Trie structure; "The dog ate," "dog ate the," "ate the bone," "the bone and," "bone and drank," and "and drank water." 

To generate the next word, we would do a depth-first search on the Trie data structure using the previous two words as keys. The result would be a collection of leaf nodes representing the possible words after the preceding two-word sequence. The leaf node includes a frequency parameter that describes the times when that particular word appeared after the two-word sequence. Given the possible words and their appearance frequency, the algorithm makes a weighted random pick based on the frequencies.

## Time and Space Complexity

The operations performed on the Trie data structure follow an O(n) linear time complexity since the preceding sequence defines an absolute path to the leaf node(s). The search operation handles only a single node at any given movement concluding a constant space complexity O(1). During the creation of the Trie structure, every node may become its prefix, inferring a linear space complexity of O(n).

To generate the following word, we first must find the possible succeeding words. As asserted in the preceding paragraph, the time complexity to find them follows an O(n) time complexity. Choosing the following word requires the iteration of every possible succeeding node (m), giving us the final time complexity of O(n+m). The space complexity for calculating the probabilities and making a choice is O(m).

## Input And Output

Following the startup, the user could generate text in a few different and change parameters affecting the underlying model. The program serves options for the training text, the degree of the chain, and the word limit for generated text. 

For generating, the user has two options.
Fully automatic, where the program creates a whole text. 
Assertively, where the user only gets recommendations from the program.
Both methods follow the disseminated model parameters; selected text, degree, and limit. 

On text or degree change, the program shows a loading screen while the program trains the underlying Marko Model. To further illuminate, the text chosen changes the entire text, and a degree shift alters the diameter of the Trie data structure.

Once the user triggers the generate event, the program, using the model and the possible user input, generates text until reaching the user-set text limit. The resulting text displays to the user in the output field.

## General Information
My major/study track is tietojenkäsittelytieteen kandidaatti (TKT).
English is the language of choice for this project.

## Sources:

Markov Chain
https://en.wikipedia.org/wiki/Markov_chain
retrieved: 10.9.2022