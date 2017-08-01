import math
import random
import fractions

pinput=raw_input("Enter plaintext: ")
lp=len(pinput)

print "\nKey"
key=list()
num=raw_input("How many elements should the Key have? (Key should contain only integers) ")
for i in range(0,int(num)):
    print "Enter Key ",i+1
    n=raw_input()
    key.append(int(n))
lk=len(key)

#print "\nInitializing S"
s=list()
for i in range(0,256):
    s.append(int(i))
#print s
#print "Initialized"

#print "\nShuffling S"
j=0
for i in range(0,255):
    j=(j+s[i]+key[i%lk])%256
    temp=s[i]
    s[i]=s[j]
    s[j]=temp
#print s
#print "Shuffled"

#print "\nShuffling S Again"
i=0
j=0
a=0
k=list()
while a<lp:
    i=(i+1)%256
    j=(j+s[i])%256
    temp=s[i]
    s[i]=s[j]
    s[j]=temp
    k.append(s[(s[i]+s[j])%256])
    a=a+1
#print "Shuffled Again\n"

print
print "Plain Text: ",pinput

i=0
cipher=list()
cipheri=list()
while i<len(pinput):
    shift=ord(pinput[i])
    x=shift^k[i]
    cipheri.append(x)
    cipher.append(chr(x))
    i=i+1
    
print "\nRC4 Encryption -> ",cipheri
print cipheri

plainText=[]
secret=[]
newM=[]
def prime(n):
    flag =0
    for x in range(n, n*200):
        flag=0
        count=0
        for y in range(2, x):
            if x%y ==0:
                flag=1     
        if flag == 0:
            p=x
            break

    return p

def revGCD(phiN):
    res=0
    
    for x in range(7, 100):
        if fractions.gcd(x, phiN)==1:
            res = x
            break
    return res

def findingK(e, d, phiN):
    k= ((e*d)-1)/phiN
    return k

    
def findingD(e, phiN):
    res=0
    for x in range(2, 100000):
        if (e*x)%phiN==1 :
            res=x
            break
    return res

def encrypt(n, e):
    
    for i in range(0,len(cipheri)):
        m=cipheri[i]
        c=(m**e)%n
        #print c
        secret.append(c)
    stri=list()
    for i in range(0, len(cipheri)):
        stri.append(secret[i])
    print "\nRSA Encryption -> ", stri

def decrypt(n, d):
    newM=list()
    for i in range(0,len(secret)):
        m =(secret[i]**d)%n
        newM.append(m)
    return newM
    
#print "Random generation of p & q ."
n = random.randint(16, 60)
p=prime(n)
q=0
n = random.randint(16, 60)
q=prime(n)
while p==q :
    n = random.randint(16, 60)
    q=prime(n)

#print "p value - ", p
#print "q value - ", q
n= p*q
phiN= (p-1)*(q-1)
#print "n value - ", n
#print "phi N - ", phiN
e= revGCD(phiN)
#print "e value : ", e
encrypt(n, e)

d=findingD(e, phiN)
#print "\nfinding D ", d
#print "tracing message back .... "
kk=findingK(e, d, phiN)
#print "k value : ", kk
newM=decrypt(n, d)
print "\nRSA Decryption -> ",newM

i=0
output=list()
while i<len(pinput):
    shift=int(newM[i])
    output.append((shift^k[i]))
    i=i+1
print "\nRC4 Decryption -> ",output
