from * import SM3
import random
import string
import math
import time
from collections import Counter


def randomnum(n):
    rn = []
    while len(rn) < n:
        i = random.randint(0, pow(2,64))
        if i not in rn:
            rn.append(i)
    return rn


n=int(input("想要产生碰撞的byte数为:"))
table=int(input("制随机数表的规模2^:"))
random_hash = []
r=randomnum(pow(2,table))
start = time.time()
tag=0
for i in range(pow(2,table)):
    M=str(r[i])
    hash_value = SM3(M)
    random_hash.append(M[:2*n])
    collision = dict(Counter(random_hash))
    for key,value in collision.items():
        if value > 1:
            tag=1
            print("前",n,"字节的碰撞已找到！")
            break
    if tag==1:#设置标志位，若碰撞产生则置1
        break
        
end = time.time()
print("用时:%.3fs"%(end-start))
