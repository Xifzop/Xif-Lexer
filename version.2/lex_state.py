
class State(object):

	def __init__(self, name, events = None):
		self.name = name
		self.events = events or {}

	'''
		is_matched_func would check whether the current state of the Analyser and value input
		 meets the condition to take the transition.
	'''
	def reg_event(self, evt_id, is_matched_func, action_func):
		self.events[evt_id] = {
			"matched_fn" : is_matched_func,
			"action_func": action_func
		}

	def trigger(self, info, matcher):
		for evt_id in self.events:
			event_package = self.events[evt_id]
			if event_package["matched_fn"](info):
				return event_package["action_func"](info, matcher)
		raise NoEventTriggeredException()