#! /usr/bin/env python

from sys import argv
from tokenize import tokenize
from io import BytesIO
from pprint import PrettyPrinter

if __name__ == "__main__":
	pp = PrettyPrinter(indent = 4, compact = True)
	pp = pp.pprint

	for arg in argv[1:]:
		valid_id = False
		br = BytesIO(arg.encode('utf-8')).readline
		t = tokenize(br)
		
		# skip encoding
		
		next(t)

		# accept NAME token

		tokenized = next(t)
		if tokenized.type == 1:
			identifier = tokenized.string
			tokenized = next(t)
			
			# make sure tokenization is terminated after the first NAME token
			# this will fail when arg is ie. 'x y'
			
			if tokenized.type == 0:
				valid_id = True

		if valid_id:
			code = 'import {}'.format(identifier)				
			env = {}
			try:
				exec(code, env)
				print(repr(env[identifier]))
				print('the following symbols were added:')
				pp(dir(env[identifier]))
				
			except ImportError:
				print('import {} failed'.format(identifier))
		else:
			print('invalid identifier: {}'.format(repr(arg)))

