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
  
  flsan = []
  for i in flsa:
  	print i
    flsan.append(i)
  if len(idx) >= 1:
  	print 'length of idx was >= 1.'
    for g in range(len(flsa)):
        print g, flsa[g]
    print '****************************************'
    for h in idx:
        for i in range(len(flsa)):
            #print flsa[i], oldformat[h-1], oldformat[h+1]
            vart = find_between(flsa[i], oldformat[h-1], oldformat[h+1])
            newstring = newformat
            newstring[h] = vart
            print vart, ''.join(newstring)
            flsan[i] = ''.join(newstring)

execute = 1
for i in range(len(flsa)):
    cmd = 'mv '+dir+flsa[i]+' '+dir+flsan[i]
    if execute == 1:
        print "Now executing: "+cmd
        subprocess.call(cmd, shell=True)
    else:
        print cmd
    


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
