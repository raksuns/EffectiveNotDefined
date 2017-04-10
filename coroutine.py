'''
range : , xrange
'''

import time
begin_t = time.time()

for i in range(300000000):
    print(i)
    break

print('{:.1f}초 소요'.format(time.time() - begin_t))


# range
def myrange(start, end, step):
    mylist = []
    while start < end:
        mylist.append(start)
        start += step
    return mylist


# xrange
def myxrange(start, end, step):
    while start < end:
        yield start  # generator 문법
        start += step

if __name__ == "__main__":
    for i in myrange(0, 10, 2):
        print('myrange : %s' % i)

    for i in myxrange(0, 10, 2):
        print('xrange : %s' % i)

# 중첩된 Generator를 Pipeline 처럼 사용할 수 있다
gen1 = (i**2 for i in range(10))
gen2 = (j+10 for j in gen1)
gen3 = (k*10 for k in gen2)

for i in gen3:
    print(i, end=' ')


