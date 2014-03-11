#! /usr/bin/env python


def is_lst(lst):
	return type(lst) is list

def car(lst):
	if is_lst(lst):
		if len(lst) == 0:
			return None
		else:
			return lst[0]
	else:
		return None

def cdr(lst):
	if is_lst(lst):
		return lst[1:]
	else:
		return None

def collect(f, lst, target):
	'''
		simlation of the accumulator function in Lisp.
		f means the operator of each element with the target,
			signature of f is f( target_result, each_element ).
		lst means the list to be processed.
		target means the initial value of the function.

		* side-effect would get involved so be careful of your operator.
	'''
	if car(lst) is None:
		return target
	else:
		return collect(f, cdr(lst), f(target, car(lst)))


# test for function collect()
if __name__ == '__main__':

	def opr(target, element):
		new_target = []
		new_target.append(element)
		return target + new_target

	print collect( opr, [1,2,3,4,5], [] )


	s = {1:9}
	print len(s)

