"""An implementation of the Vigenere cipher."""
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

self=raw_input()
key=raw_input()
cipher=encipher(self,key)
print cipher
plain=decipher(cipher,key)
print plain
