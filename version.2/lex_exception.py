
class NotMatchedException(Exception):
	def __init__(self, info):
		info = "Unmatched for %s" % info
		super(NotMatchedException, self).__init__(info)

class NoEventTriggeredException(Exception):
	def __init__(self):
		info = "No event triggered."