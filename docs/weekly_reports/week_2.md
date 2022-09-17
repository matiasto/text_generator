Week 2
---

## Feats

- Basic Markov Chain
- Service for reading book data
- Service for cleaning the data
- Basic level text generation
- Test coverage
- Docstring

---

## Progresion

The project has taken its' elementary state. Currently, the program has; different datasets (books) to train the Markov chain, tools to clean and tokenize the raw data, and a way to generate text from that model.

---

## Learning

The learning consisted mainly of new information about Markov chains, as I was already familiar with text handling. I learned about various properties of Markov chains that may not be directly applicable to this project. One example of such thing introduced a theorem to predicting a state after n transitions. It was fascinating to see how using the Chapman-Kolmogorov Theorem, we can easily calculate the matrix showing the probability of being in a particular state after n steps. 

---

## Complications

For me, one complication remains about trie data structure. In particular, I've had difficulty figuring out where to apply this data structure effectively. One area where it makes sense (in my mind) is suggesting the initial word to use in the Markov chain. Almost all examples I found on the web utilize a trie data structure in word completion. I can't wrap my head around using this data structure to store a graph like the Markov chain. I could use a hint on where and possibly how to apply trie data structure to this program. Currently, I'm using a dictionary as a kind of placeholder.

---

## Following Steps

Further steps include the implementation of a trie data structure and a way to alter the degree of the Markov chain. If time allows, possible UI components will begin to take shape.
