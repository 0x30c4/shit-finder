#!/usr/bin/python3
import argparse
import os

parser = argparse.ArgumentParser('shit_finder', description='Search for file and pattern in a mlocate database.')

parser.add_argument('file_name', help='name of the file or directory\
					that you wanna find')

parser.add_argument('-d', '--dir-name', help='the directory in which \
					the search will be procured.if directory \
					is specified then the search will procured from \
					the current directory')

parser.add_argument('-i', '--ignore-case', help='ignore case distinctions \
					when matching patterns', action="store_true")

parser.add_argument('-c', '--count', help='only print number of \
					found entries', action="store_true")

args = parser.parse_args()

if args.dir_name:
	dir_name = args.dir_name

else:
	dir_name = os.getcwd()

file_path_list = [f'{i[0]}/{j}' for i in os.walk(dir_name) for j in i[2]]
search_result = [i for i in file_path_list if not i.find(args.file_name) == -1]

if args.ignore_case:
	search_result = [i.lower() for i in file_path_list if not i.find(args.file_name.lower()) == -1]

if args.count:
	print(len(search_result))

else:
	for i in search_result:
		print(i)