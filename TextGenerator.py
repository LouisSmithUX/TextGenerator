#Owner Louis Smith

# import argparse
import nltk
from collections import defaultdict
import random


class Main() :
	def __init__(self): 

		with open("data.txt","r") as data:
			self.words = nltk.word_tokenize(data.read())

		self.bigramFreq = self.buildBigramFreq(self.words)

		currentWord = self.getMostCommon(self.words)
		for i in range(50):
			print (currentWord, end= ' ')
			randomIndex = random.random()
			for keyIntervals,valIntervals in self.bigramFreq[currentWord].items():
				if randomIndex>keyIntervals[0] and randomIndex<keyIntervals[1]:
					currentWord = valIntervals


	def buildBigramFreq(self, words):
			bigrams = list(nltk.bigrams(words))

			spread = defaultdict(lambda: [])

			for bigram in bigrams:
				spread[bigram[0]].append(bigram[1])

			for key,val in spread.items():
				totalNumberOfValues = len(val)
				probabilityChunks = defaultdict(lambda: 0)
				runningTotal = 0
				for v in set(val):
					proportion = val.count(v)/totalNumberOfValues
					probabilityChunks[(runningTotal,runningTotal+proportion)] = v
					runningTotal += proportion
				spread[key] = probabilityChunks

			return spread

# 			def generate_model(cfdist, word, num=15):
#     for i in range(num):
#         print(word, end=' ')
#         word = cfdist[word].max()

# text = nltk.corpus.genesis.words('english-kjv.txt')
# bigrams = nltk.bigrams(text)
# cfd = nltk.ConditionalFreqDist(bigrams) [1]
 	
# >>> cfd['living']
# FreqDist({'creature': 7, 'thing': 4, 'substance': 2, ',': 1, '.': 1, 'soul': 1})
# >>> generate_model(cfd, 'living')
# living creature that he said , and the land of the land of the land

	def getMostCommon(self,words):
			return nltk.FreqDist(words).most_common()[0][0]



if __name__=="__main__":
	launcher = Main()
