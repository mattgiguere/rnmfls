"""
Created on Wed Mar 12 21:34:46 2014

@author: mattgiguere


INPUT: This code is designed to take take a directory,
a current filename format and the desired filename format
as input.

OUTPUT: Renamed files in the specified format


"""
from __future__ import division, print_function
import sys
import subprocess
try:
    import numpy as np
except ImportError:
    print('You need numpy installed')
    sys.exit(1)

__version__ = '0.0.1'


def find_between( s, first, last ):
  try:
    start = s.index( first ) + len( first )
    end = s.index( last, start )
    return s[start:end]
  except ValueError:
    return ""



def rnm(fnm_dir,old_fnm, new_fnm):
  execute = 0
  import subprocess
  fls = subprocess.check_output(["ls", "-1", fnm_dir])
  flsa = fls.split('\n')
  flsa = flsa[0:len(flsa)-1]

  substr = 'var'
  idx = -1
  for i in range(len(oldformat)):
    if oldformat[i] == 'var':
      if newformat[i] == 'var':
        idx = [idx, i]
      else:
        print "WARNING! var in new and old format must be in same location!"

  idx = idx[1::]







if __name__ == '__main__':
    if len(sys.argv) == 1:
        print('')
        print('python rnm.py directory current_filename new_filename')
        print('')
        sys.exit(2)
    elif len(sys.argv) != 4:
        print('use the command')
        print('python rnm.py directory current_filename new_filename')
        sys.exit(2)

    new_fnm = str(sys.argv[3])
    old_fnm = str(sys.argv[2])
    fnm_dir = str(sys.argv[1])

    rnm(directory, old_fnm, new_fnm)
