
print "Modified RC4 Encryption\n"

p=raw_input("Enter plaintext: ")
lp=len(p)

print "\nEnter Key 1 (RC4)"
ss1=raw_input()
key1=list()
for i in range(0,len(ss1)):
    key1.append(ord(ss1[i]))
#print key1
lk1=len(key1)

print "\nEnter Key 2 (RC4)"
ss2=raw_input()
key2=list()
for i in range(0,len(ss2)):
    key2.append(ord(ss2[i]))
#print key2
lk2=len(key2)


#print "\nInitializing S"
s1=list()
s2=list()
for i in range(0,256):
    s1.append(int(i))
    s2.append(int(i))
#print s1
print
#print s2
#print "Initialized"

#print "\nShuffling S"
j1=0
j2=0
for i in range(0,255):
    j1=(j1+s1[i]+key1[i%lk1])%256
    s1[i],s1[j1]=s1[j1],s1[i]
    j2=(j2+s2[i]+key2[i%lk2])%256
    s2[i],s2[j2]=s2[j2],s2[i]
#print s1
print
#print s2
#print "Shuffled"

#print "\nPRGA"
#print "\nShuffling S Again"
i=0
j1=0
j2=0
a=0
k=list()
while a<lp:
    i=(i+1)%256
    j1=(j1+s1[i])%256
    s1[i],s1[j1]=s1[j1],s1[i]
    j2=(j2+s2[i])%256
    s2[i],s2[j2]=s2[j2],s2[i]
    stream1=s1[(s1[i]+s1[j1])%256]
    stream2=s2[(s2[i]+s2[j2])%256]

    s1[s2[j1]],s1[s2[j2]]=s1[s2[j2]],s1[s2[j1]]
    s2[s1[j1]],s2[s1[j2]]=s2[s1[j2]],s2[s1[j1]]

    
    k.append(stream1^stream2)
    a=a+1
#print "Shuffled Again\n"

print "Plain Text: ",p
print "Key: ",k

i=0
cipher=list()
cipheri=list()
while i<len(p):
    shift=ord(p[i])
    x=shift^k[i]
    
    cipheri.append(x)
    
    cipher.append(chr(x))
    i=i+1
    
#print "Cipher list",cipheri
cc=''.join(cipher)
#print "\nCipher Text ",cc


def encipher(self, key):
        """Encipher input (plaintext) using the Vigenere cipher and return
           it (ciphertext)."""
        ciphertext = []
        k = 0
        n = len(key)
        for i in range(len(self)):
            p = self[i]
            if p.isalpha():
                ciphertext.append(chr((ord(p) + ord(
                (key[k % n].upper(), key[k % n].lower())[int(p.islower())]
                ) - 2*ord('Aa'[int(p.islower())])) % 26 +
                ord('Aa'[int(p.islower())])))
                k += 1
            else:
                ciphertext.append(p)
        return (''.join(ciphertext))

def decipher(self, key):
        """Decipher input (ciphertext) using the Vigenere cipher and return
           it (plaintext)."""
        plaintext = []
        k = 0
        n = len(key)
        for i in range(len(self)):
            c = self[i]
            if c.isalpha():
                plaintext.append(chr((ord(c) - ord(
                (key[k % n].upper(), key[k % n].lower())[int(c.islower())]
                )) % 26 + ord('Aa'[int(c.islower())])))
                k += 1
            else:
                plaintext.append(c)
        return (''.join(plaintext))

    
print "\nEnter Key 3 (Vigniere)"
key=raw_input()
ciphers=encipher(cc,key)
print "\nEncryption",ciphers
p=decipher(ciphers,key)
#print "\nDecryption",p

i=0
output=list()
while i<len(p):
    shift=ord(cipher[i])
    output.append(chr(shift^k[i]))
    i=i+1
plain=''.join(output)
print "\nDecryption",plain
