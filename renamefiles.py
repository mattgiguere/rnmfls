#
#c. 2014.03.07 MJG

### a simple script to rename files
from __future__ import division, print_function
import sys

try:
    import rnmfls
except ImportError:
    print('You need rnmfls installed')
    sys.exit(1)

import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Renames files.')
    parser.add_argument('prefix',
        help='Current prefix for all files you want to change. \
        Make sure you are in the correct directory!', type=str)
    parser.add_argument('prefix',
        help='Name of input csv file with targets, column are \
        Ra_degrees, Dec_degrees, Kepmag', type=str)
    parser.add_argument('campaign',
        help='K2 Campaign number', type=int)
    args = parser.parse_args()

    rnmfls.rnm(args.prefix,args.campaign)


