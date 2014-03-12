from lex_analyser import *
from lex_exception import *

class Util(object):
	@staticmethod
	def read_file(fpath, block_size=1):
		EOF = ' '
		with open(fpath, 'r') as f:
			while 1:
				block = f.read(block_size)
				if block:
					yield block
				else:
					yield EOF
					break


def init_states():

		empty_state     = State("empty")
		done_state      = State("done")
		with_char_state = State("with_char")
		error_state     = State("error")

		states = {
			empty_state.name     : empty_state,
			done_state.name      : done_state,
			with_char_state.name : with_char_state,
			error_state.name     : error_state
		}


		# callbacks for empty state
		def empty_get_char_matched(info):
			return not PatternMatcher.match_whole(r'\s', info[LexAnalyser.LAST_CHAR] )

		def empty_get_char_action(info, matcher):
			info[LexAnalyser.CURRENT_STR]  = info[LexAnalyser.LAST_CHAR]
			info[LexAnalyser.PREV_MATCHED] = matcher.match(info[LexAnalyser.CURRENT_STR])
			return "with_char"

		def empty_get_space_matched(info):
			return PatternMatcher.match_whole(r'\s', info[LexAnalyser.LAST_CHAR])

		def empty_get_space_action(info, matcher):
			return "empty"
		# end of callbacks defined for empty state.

		# callbacks for with-char state
		def with_char_get_char_matched(info):
			current_ch = info[LexAnalyser.LAST_CHAR]
			return not PatternMatcher.match_whole(r'\s', current_ch)

			
		def with_char_get_char_action(info, matcher):
			current_ch = info[LexAnalyser.LAST_CHAR]
			current_str = info[LexAnalyser.CURRENT_STR]

			result = matcher.match(current_str + current_ch)

			if result:
				info[LexAnalyser.PREV_MATCHED] = result
				info[LexAnalyser.CURRENT_STR] += current_ch
				return "with_char"
			else:
				if info[LexAnalyser.PREV_MATCHED]:
					info[LexAnalyser.NEXT_TERM]   = current_str
					info[LexAnalyser.TERM_TYPE]   = info[LexAnalyser.PREV_MATCHED]
					info[LexAnalyser.CURRENT_STR] = current_ch
					info[LexAnalyser.PREV_MATCHED] = matcher.match(info[LexAnalyser.CURRENT_STR])
					return "with_char"
				else:
					info[LexAnalyser.CURRENT_STR] += current_ch
					info[LexAnalyser.PREV_MATCHED] = False
					return "with_char"
					#raise NotMatchedException(info[LexAnalyser.CURRENT_STR])


		def with_char_get_space_matched(info):
			current_ch = info[LexAnalyser.LAST_CHAR]
			return PatternMatcher.match_whole(r'\s', current_ch)

		def with_char_get_space_action(info, matcher):
			current_ch = info[LexAnalyser.LAST_CHAR]
			current_str = info[LexAnalyser.CURRENT_STR]
			result = matcher.match(current_str)

			if result:
				info[LexAnalyser.NEXT_TERM]    = current_str
				info[LexAnalyser.TERM_TYPE]    = result
				info[LexAnalyser.CURRENT_STR]  = ""
				info[LexAnalyser.PREV_MATCHED] = False
				return "empty" 
			else:
				# case for string type..
				if info[LexAnalyser.CURRENT_STR][0] == '"':
					info[LexAnalyser.CURRENT_STR] += current_ch
					info[LexAnalyser.PREV_MATCHED] = False 
					return "with_char"
				else:
					raise NotMatchedException(info[LexAnalyser.CURRENT_STR])

		# end of callbacks defined for with-char state.
		empty_state.reg_event( "get_char", empty_get_char_matched, empty_get_char_action)
		empty_state.reg_event( "get_space", empty_get_space_matched, empty_get_space_action)
		with_char_state.reg_event( "get_space", with_char_get_space_matched, with_char_get_space_action )
		with_char_state.reg_event( "get_char", with_char_get_char_matched, with_char_get_char_action)

		return states