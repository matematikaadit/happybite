from glob import glob
import time
import subprocess as subp

def bench(f):
    start = time.perf_counter()
    f()
    end = time.perf_counter()
    return end - start

for script in sorted(glob('???.py')):
    d = bench(lambda :subp.call(['python3',script],stdout=subp.DEVNULL))
    if d > 1:
        print("{} ({:.1f} s)".format(script,d))