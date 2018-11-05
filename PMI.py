# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 17:29:59 2018

@author: mnaik
"""
import nltk
from nltk.collocations import *
from nltk.corpus import stopwords 
text = open('D:/mayur/Masters/Text Analytics/assignment 4/Question1.txt')
rawtext = text.read()
stop = stopwords.words('english')
sw = [i for i in rawtext.split() if i not in stop]
bigram_measures = nltk.collocations.BigramAssocMeasures()
finder = BigramCollocationFinder.from_words(sw)
scored = finder.score_ngrams(bigram_measures.pmi)
print("scores are -----", scored)    
finder.nbest(bigram_measures.pmi, 10)
finder.apply_freq_filter(2)
B = finder.nbest(bigram_measures.pmi, 10)  
print(B)
