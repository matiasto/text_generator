# Requirements Specification

---

The text generator aims to accomplish natural language generation using Markov chains.

## Language

The primary programming language used is Python. Other proficient languages include JavaScript. 

## Algorithms

The program primarily relies on a stochastic model called the Markov chain. The model describes a sequence of possible events, where every event in that sequence only depends on the predetermined number of previous events. Transitions from the initial state to the next derive from the transition matrix, which describes the probabilities of said transitions. Because of this, the algorithm itself runs in linear time and constant space.

## Input And Output

In an ideal case, the user can download a text of their choice, and the program will create the transition matrix from that input. Following the initialization, the user could generate text in a few different ways. The order of importance for these ways is in the order of mention. Fully automatic, where the program creates a whole text. Semi-automatically, where the user can add their own words/sentences. Assertively, where the user only gets recommendations from the program.

Firstly the input file requires a reliable way of tokenizing. Secondly, it needs to calculate/create the transition matrix. Once done, the program should work fine in automatic mode. Other challenges arise once user input comes into play. The handling of imperfect user input requires regular expression and a way to find closely matched words. One great tool for this is the use of Levenshtein distance.

## General Information
My major/study track is tietojenkäsittelytieteen kandidaatti (TKT).
English is the language of choice for this project.

## Sources:

Markov Chain
https://en.wikipedia.org/wiki/Markov_chain
retrieved: 10.9.2022