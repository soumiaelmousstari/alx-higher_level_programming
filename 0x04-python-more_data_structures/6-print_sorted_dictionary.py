#!/usr/bin/python3
def print_sort_dictionary(a_dictionary):
    for i in sorted(a_dictionary.keys()):
        print("{}: {}".format(i, a_dictionary[i]))
