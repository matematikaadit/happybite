from glob import glob
import time
import subprocess as subp

def bench(f,*arg):
    start = time.perf_counter()
    f(*arg)
    end = time.perf_counter()
    return end - start

fs = sorted(glob('???.py'))
cmd = lambda s:subp.call(['python3',s],stdout=subp.DEVNULL)
def run(fs=fs):
    for script in fs:
        d = bench(cmd,script)
        if d > 1:
            print("{} ({:.1f} s)".format(script,d))

if __name__ == '__main__':
    run()