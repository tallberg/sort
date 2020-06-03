#!/usr/bin/env python3
import sys
import numpy as np
from timeit import default_timer as timer
name = sys.argv[1] if len(sys.argv) > 1 else input('filename?')
start = timer()
np.memmap(name, dtype=np.float16).sort(kind='merge')
end = timer()
print(end - start)
if '-p' in sys.argv:
  print(np.memmap(name, dtype=np.float16).tolist())
