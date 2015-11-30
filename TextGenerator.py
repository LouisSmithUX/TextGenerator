#Owner Louis Smith

# import argparse
import argparse
import nltk
from collections import defaultdict
import numpy


class Main() :
	def __init__(self): 

		parser = argparse.ArgumentParser(description='Input txt file.')
		parser.add_argument('texts', metavar='i', type=str, nargs='+',
	                   help='input text')

		parser.parse_args(namespace=self)

		self.words=[]
		for text in self.texts:
			try:
				with open(text,"r") as data:
					self.words += [w for w in nltk.word_tokenize(data.read()) if not w.isnumeric()]
			except FileNotFoundError:
				print("That's not a file you moron!")
				raise SystemExit()

		self.bigramFreq = self.buildBigramFreq(self.words)

		currentWord = self.getMostCommon(self.words)

		self.generate(self.bigramFreq,currentWord)

	def buildBigramFreq(self, words):
		bigrams = list(nltk.bigrams(words))

		cfdist = nltk.ConditionalFreqDist(bigrams)
		for word,wordFreqDist in cfdist.items():
			sumTotal = sum(wordFreqDist.values())
			for bigramword,prob in wordFreqDist.items():
				cfdist[word][bigramword] = prob/sumTotal

		return cfdist

	def generate(self,cfdist, word, num=150):
		for i in range(num):
			print(word, end=' ')
			nextWords,weights = list(zip(*[(word,prob) for word,prob in cfdist[word].items()]))
			word = numpy.random.choice(nextWords,p=weights)

	def getMostCommon(self,words):
			return nltk.FreqDist(words).most_common()[0][0]



if __name__=="__main__":
	launcher = Main()
