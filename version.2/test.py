#! /usr/bin/env python

from lex import *

if __name__ == '__main__':
	xif = Lexer()
	xif.load_patterns('patterns.json')
	for term in xif.analyse('test.in'):
	 	print term