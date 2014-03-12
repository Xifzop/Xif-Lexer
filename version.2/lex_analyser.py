from lex_matcher import *
from lex_state   import *
from lex_exception import NotMatchedException

class LexAnalyser(object):

	# Enumerator of the possible state of the machine [ Lexical Analysis ].
	ESCAPE          = 19
	STRING_TYPE     = 18
	TERM_TYPE       = 17
	CURRENT_STATE   = 16
	LAST_CHAR       = 15
	NEXT_TERM       = 14
	STATES          = 13
	CURRENT_STR     = 12
	PREV_MATCHED    = 11

	def __init__(self, states, current_state_name, pattern=PatternMatcher()):
		self.info = {
			self.ESCAPE          : False,
			self.STRING_TYPE     : False,
			self.PREV_MATCHED    : False,
			self.CURRENT_STR     : "",
			self.STATES          : states,
			self.CURRENT_STATE   : states[current_state_name],
			self.NEXT_TERM       : None,
			self.TERM_TYPE       : None,
			self.LAST_CHAR       : None
		}
		self.matcher = pattern


	def do_lex(self, source):
		for ch in source:
			self.info[self.LAST_CHAR] = ch
			target = self.info[self.CURRENT_STATE].trigger(self.info, self.matcher)
			self.info[self.CURRENT_STATE] = self.info[self.STATES][target]
			if self.info[self.NEXT_TERM]:
				yield ( self.info[self.TERM_TYPE] ,self.info[self.NEXT_TERM] )
				self.info[self.TERM_TYPE] = None
				self.info[self.NEXT_TERM] = None
			else:
				continue

		if not self.info[self.NEXT_TERM]:
			raise NotMatchedException(self.info[self.CURRENT_STR])
