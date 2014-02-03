#!/usr/bin/env python

__author__ = 'christian'

import sys
import os
import pprint

# Generator that gets all files within a path relatively
def list_file_tree(path):

    absolute_path = os.path.abspath(path)

    for root, dirs, filenames in os.walk(absolute_path):
        for f in filenames:
            yield os.path.relpath(os.path.join(root,f),absolute_path)




def main():

    fileset_list = []

    # get files in every directory
    for path in sys.argv[1:]:
        fileset_list.append(
            set(list_file_tree(path))
    )

    # get matchin paths for all sets
    result = fileset_list[0]
    for fileset in fileset_list[1:]:
        result &= fileset

    result_list = list(result)
    result_list.sort()

    pprint.pprint(result_list)

if __name__ == "__main__":
    main()