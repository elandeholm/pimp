#! /usr/bin/env python

from sys import argv
from pprint import PrettyPrinter
from keyword import iskeyword

if __name__ == "__main__":
	pp = PrettyPrinter(indent = 4, compact = True).pprint

	for arg in argv[1:]:
		if arg.isidentifier():
			if not iskeyword(arg):
				code = 'import {}'.format(arg)				
				env = {}
				try:
					exec(code, env)
					print(repr(env[arg]))
					print('the following symbols were added:')
					pp(dir(env[arg]))
				
				except ImportError:
					print('import {} failed'.format(arg))
			else:
				print('\'{}\' is a python keyword'.format(arg))
		else:
			print('invalid identifier: {}'.format(repr(arg)))

