#!/usr/bin/env python3
import sys
import random
import struct
import math
import numpy as np
from array import array
from timeit import default_timer as timer

def nrand(n):
  while n > 0:
      yield random.uniform(-1000, 1000)
      n = n - 1

def nrands(n):
  while n > 0:
      yield str(random.uniform(-1000, 1000))
      n = n - 1

def F4(name, n):
  print('float32 to binary using generator')
  step = n if n < 1000 else 1000
  file = open(name, 'wb')
  for __ in range(0, n, step):
      array('f', list(nrand(step))).tofile(file)
  file.close()

def F2(name, n):
  print('float16 to binary')
  start = timer()
  step = n if n < 1000 else 1000
  a = np.empty(step, dtype=np.float16)
  file = open(name, 'wb')  
  for __ in range(0, n, step):
    a[:] = np.random.normal(scale=1000, size=step)
    a.tofile(file)
  file.close()
  end = timer()
  print("Generated {:,} values in {:.6f} seconds".format(n, end - start))


n = int(sys.argv[1]) if len(sys.argv) > 1 else int(input('how many values (10^x)? '))
name = sys.argv[2] if len(sys.argv) > 2 else input('filename?')

if len(name) == 0:
  print(list(nrand(n)))
else: 
  if n > 9:
    print("Value is to large: 10^{}. max value is 9 (1,000,000,000)".format(n))
    n = math.floor(math.log10(n))
    print("Using log10() = {}".format(n))    
  n = int(math.pow(10, n))  
  F2(name, n)
  
  


