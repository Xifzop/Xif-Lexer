#! /usr/bin/env python

class XStack(list):
	def __init__(self):
		pass

	def push(self, el):
		self.append(el)
		return self

	def pop(self):
		top_val = self[-1]
		self = self[:-1]
		return top_val


# test for the utility function above
stack = XStack()
print stack
print stack.push(1)
print stack.push(2)
print stack.push(3)
print stack.pop()