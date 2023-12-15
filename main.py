import sys
from functools import cache
import time

start_time = time.time()

sys.setrecursionlimit(1000000)
input = sys.stdin.readline

class Solution:
    def __init__(self, line):
        part = 2
        s, gr = line.split()
        if part == 1:
            self.s = s # add end char
        else:
            self.s = ''
            for i in range(5):
                self.s += s
                if i != 4:
                    self.s += '?'
        self.s += '$'

        if part == 1:
            self.gr = tuple(map(int, gr.split(',')))
        else:
            self.gr = tuple(map(int, gr.split(',')*5))

    @cache # dynamic programming
    def dp(self, pos=0, cnt=0, cg=0): # start search at index 0 (pos = 0), cur group # cnt = 0, cur group starts at index 0
        if pos == len(self.s)-1:
            # done (remember extra char at end which is .)
            return cg == len(self.gr) or (cg == len(self.gr)-1 and cnt == self.gr[cg]) # all the groups have been fulfilled
        if cg == len(self.gr): # cg index is greater than max self.gr index
            return '#' not in self.s[pos:] # if any more #, then there must have be a surplus
        c = self.s[pos]
        if c == '#':
            return self.dp(pos+1, cnt+1, cg) if cnt+1 <= self.gr[cg] else 0
        elif c == '.':
            if cnt == 0:
                return self.dp(pos+1, cnt, cg)
            else:
                return self.dp(pos+1, 0, cg+1) if cnt == self.gr[cg] else 0
        else:
            # consider if it is # or .
            # first bracket if it is # and second bracket if it is .
            return (self.dp(pos+1, cnt+1, cg) if cnt+1 <= self.gr[cg] else 0) + (self.dp(pos+1, cnt, cg) if cnt == 0 else (self.dp(pos+1, 0, cg+1) if cnt == self.gr[cg] else 0))


ans = 0
with open('file.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        soln = Solution(line)
        ans += soln.dp()

print(ans)

end_time = time.time()

print(round((end_time - start_time) * 1000, 5), 'ms')