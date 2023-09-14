
a = (lambda x, y : x**y)(10, 3)

print(a)


def e_is_fun(l):
    return l[0]*l[1]

a = [[1,2], [3,2],[4,2]]

a[0][1] = 6 
print(a)

b =  tuple(a)
k = map(e_is_fun, a )
print(type(k))

class C(object):
    pass

c= C()

print(type(c))

p = "Python"

sp = p[1:3]
print(sp)

stem_leaf = [[],[],[]]
score = [0,0,2,4,7,8,9]
score += [11,11,13,18]
score += [20]

for i in score :
    d, m = divmod(i,10)
    stem_leaf[d].append(m)


index =0
for ll in stem_leaf :
    print(index, " :", ll)
    index += 1

def sumofDigits(num) :
    digits = tuple(map(int,list(str(num))))
    print(digits)
    return sum(digits)
    

print(sumofDigits(33451236))

  
    