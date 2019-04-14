#!/usr/bin/env python
### ARGUMENTS USING PYTHON ###
# include standard modules
import argparse

# initiate the parser
parser = argparse.ArgumentParser()

# add long and short argument
# Args with parameters
parser.add_argument("--width", "-w", help="set output width")

## Static Args
parser.add_argument("-V", "--version", help="show program version", action="store_true")

# read arguments from the command line
args = parser.parse_args()

# check for --width
if args.width:  
    print("set output width to %s" % args.width)
elif args.version:
    print("Version asked")
