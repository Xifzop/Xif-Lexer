#! /usr/bin/env python
from lex_util import *

# Created by Tony H. Improved support for String. But not for escape.

class Lexer(object):

	VERSION = 1.1 
	STATES  = init_states()

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