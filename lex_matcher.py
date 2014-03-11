
class Pattern(object):
	def __init__(self, key, val):
		if key is not None and val is not None:
			self.id   = key
			self.form = str(val)


class PatternMatcher(object):

	@staticmethod
	def match_whole(pattern, target):
		import re
		pattern = re.compile(pattern)
		return pattern.match(target)

	def __init__(self):
		self._patterns = {}

	def __iadd__(self, pattern):
		import re
		ptn = r'\s' + pattern.form + r'\s'
		ptn = re.compile(ptn)
		self._patterns[pattern.id] = ptn
		return self

	def match(self, val):
		val = "".join([' ', val, ' '])
		for ptn_id in self._patterns:
			if self._patterns[ptn_id].match(val):
				return ptn_id
			else:
				continue
		return None

