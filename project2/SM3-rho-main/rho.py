from * import SM3
import random
import string
import time

n=int(input("想要寻找前多少bit的碰撞："))
start = time.time()
r1 = str(random.randint(0, pow(2,64)))
hash_value=[]
while 1:
    r1_sm3=SM3(r1)
    if(r1_sm3[:4] in hash_value):
        print("已找到前",n,"bit碰撞！")
        break
    hash_value.append(r1_sm3[:4])
    r1=SM3(r1)
end = time.time()
print("用时:%.3fs"%(end-start))
