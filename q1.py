#1.1
def AND(p, q):
    return p and q

#1.2
def OR(p,q):
    return p or q

#1.3
def IF(p,q):
    return OR(AND(p, q), NOT(p))

#1.4
def NOT(p):
    return not p
#1.5
def IFF(p,q):
#    return OR(AND(p, q), OR(NOT(p))
    return ((p and q) or  ( not p and not q))

#p = True
#q = True
#print(IF(p, q))
#p = False
#q = False
#print(IF(p, q))
#p = True
#q = True
#print(IF(p, q))
#p = False
#q = True
#print(IF(p, q))

p = True
q = False
print "Simple Evaluation Function Test"
print "p =", p
print "q =", q
print "(p or q):   "
print(OR(p,q))
print "(p and q):  "
print(AND(p,q))
print "(p -> q):   "
print (IF(p,q))
print "(p <-> q):  "
print (IFF(p,q))
print "-p:         "
print (NOT(p))
