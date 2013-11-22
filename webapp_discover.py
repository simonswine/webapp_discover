#!/usr/bin/env python3

__author__ = 'christian'

import webapp_discover
import sys


def main():

    discover_dir = sys.argv[1]
    print("Running discovery in %s" % discover_dir)

    expl = webapp_discover.Explorer()
    expl.run(discover_dir)


if __name__ == "__main__":
    main()
