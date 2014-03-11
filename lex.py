#! /usr/bin/env python
from lex_util import *

class Lexer(object):

	STATES = init_states()

	def __init__(self):
		self.matcher  = PatternMatcher()
		self.analyser = LexAnalyser( self.STATES, "empty", pattern=self.matcher )

	def analyse(self, fpath):
		source = Util.read_file(fpath)	
		for term in self.analyser.do_lex(source):
			yield term

	'''
		load file pattern in file whose format is .json.
	'''
	def load_patterns(self, fpath=None):
		import json
		if fpath:
			# load patterns from json file
			with open(fpath, 'r') as fjson:
				patterns = json.loads(fjson.read())
				for ptn in patterns:
					if len(ptn):
						print ptn
						ptn = ptn.items()[0]
						self.matcher += Pattern(*ptn)
			return True
		else:
			return False

	'''
		reset the pattern matcher
	'''
	def clean_patterns(self):
		self.pattern = PatternMatcher()


# Do lexical Analysing ..
if __name__ == '__main__':	
	l = Lexer()

	# l.matcher += Pattern('Int', r'([1-9][0-9]*)?[0-9]')
	# l.matcher += Pattern('Var', r'[A-Za-z]+')
	# l.matcher += Pattern('Float', r'([1-9][0-9]*)?[0-9]\.[0-9]*')
	# l.matcher += Pattern('Plus', r'\+')
	# l.matcher += Pattern('Left', r'\[')
	# l.matcher += Pattern('Right', r'\]')
	# l.matcher += Pattern('semi', r';')

	# for term in l.analyse('test.in'):
	# 	print term
	l.load_patterns('patterns.json')