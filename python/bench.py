from glob import glob
import time
import subprocess as subp

def bench(f,*arg):
    start = time.perf_counter()
    f(*arg)
    end = time.perf_counter()
    return end - start

fs = sorted(glob('p???.py'))
cmd = lambda s:subp.call(['python3',s],stdout=subp.DEVNULL)
def run(fs=fs):
    for script in fs:
        d = bench(cmd,script)
        if d > 1:
            print("{} ({:.1f} s)".format(script,d))

import sys
TIME_LIMIT = 60 # second
if __name__ == '__main__':
    if len(sys.argv) > TIME_LIMIT:
        run(sys.argv[1:])
    else:
        run()
