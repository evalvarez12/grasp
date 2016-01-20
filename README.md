# Humble Lexicon
Spanish

[![Build Status](https://travis-ci.org/evalvarez12/Simple-Lexicon.svg?branch=master)](https://travis-ci.org/evalvarez12/Humble-Lexicon)


Objective
=========

To have a machine capable of translating complicated phrases and words into simple ones. Understanding simple
as using the most common words in Spanish.

Development
===========

The first step is to recognize which words or phrases are uncommon. To do so we need to process large
amounts of text and keep count of all the words found. 

Once we have identified what needs to be simplified we need to build a substantial corpus of synonims or alternate uses 
of such phrases/words. 
Using n-grams we and the traininng text we can replace the uncommon text by common one which has the highest 
probability of appearing in text.


