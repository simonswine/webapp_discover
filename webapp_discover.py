#!/usr/bin/env python

__author__ = 'christian'

import webapp_discover
import sys
import argparse
import os


# Directory argparse (https://gist.github.com/brantfaircloth/1443543)
class FullPaths(argparse.Action):
    """Expand user- and relative-paths"""
    def __call__(self, parser, namespace, values, option_string=None):
        setattr(namespace, self.dest, os.path.abspath(os.path.expanduser(values)))

def is_dir(dirname):
    """Checks if a path is an actual directory"""
    if not os.path.isdir(dirname):
        msg = "{0} is not a directory".format(dirname)
        raise argparse.ArgumentTypeError(msg)
    else:
        return dirname

def is_ratio(ratio):
    ratio = float(ratio)
    if ratio < 0 or ratio > 1:
        raise argparse.ArgumentError("{0} must be a float between 0 and 1")
    return ratio

def is_depth(depth):
    depth = int(depth)
    if depth < 1:
        raise argparse.ArgumentError("{0} must be a int greater than 0")
    return depth




def main():

    parser = argparse.ArgumentParser()

    parser.add_argument(
        "path",
        help="specify path to scan",
        action=FullPaths,
        type=is_dir
    )

    parser.add_argument(
        "--depth",
        '-d',
        help="depth of directory recursion {1..inf}",
        type=is_depth,
        default=4
    )

    parser.add_argument(
        "--ratio",
        '-r',
        help="ratio for detection of a webapp {0..1}",
        type=float,
        default=0.7
    )


    args = parser.parse_args()
    #print args

    discover_dir = args.path
    print("Running discovery in %s" % discover_dir)

    expl = webapp_discover.Explorer()
    expl.run(discover_dir,ratio=args.ratio,level=args.depth)


if __name__ == "__main__":
    main()
