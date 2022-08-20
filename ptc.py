import math
import os
import random
import re
import sys
# Complete the 'separateNumbers' function below.
# The function accepts STRING s as parameter.
def separateNumbers(s):
    # Write your code here
    n_s = ''
    n = len(s)
    for i in s[:-1]:
        n_s += i
        a = int(n_s)
        n_ss = ''
        while(len(n_ss) < n):
            n_ss += str(a)
            a += 1
        if(len(n_ss) == n and n_ss == s):
            print('YES', n_s)
            break
    else:
        print('NO')                     
if __name__ == '__main__':
    q = int(input().strip())
    for q_itr in range(q):
        s = input()
        separateNumbers(s)