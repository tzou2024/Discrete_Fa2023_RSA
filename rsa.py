# function to generate random prime integer
import random 
from primePy import primes
from math import gcd as bltin_gcd
from functools import lru_cache
import math

# Memoized using LRU Cache
# @lru_cache(maxsize=None)
def generate_primes(min, max):
    """
    Generate a random prime number within the given range.

    min: Minimum value for the range.
    max: Maximum value for the range.

    Returns:
    Random prime number within the specified range.
    """
    available = primes.between(min, max)
    print("checking rpimes uniqueness: ", len(available) == len(set(available)))
    return random.sample(available,2)

def coprime2(a, b):
    """
    Check if two numbers are coprime using greatest common dominators.

    a: First number.
    b: Second number.

    Returns:
    True if the numbers are coprime, False otherwise.
    """
    return bltin_gcd(a, b) == 1

def mod_inverse(e, phi):
    """
    Calculate the modular multiplicative inverse of 'e' modulo 'phi'.
    
    e: Number for which the inverse is calculated.
    phi: Euler's totient function value.

    Returns:
    Modular multiplicative inverse of 'e' modulo 'phi'.
    """
    for d in range(3, phi):
        if (d * e) % phi == 1:
            return d
    return ValueError

def euler_totient(p, q):
    """
    Calculate Euler's Totient function (phi) for the given primes p and q.
    
    p: First prime number.
    q: Second prime number.

    Returns:
    Euler's Totient function value for p and q.
    """
    #I think that this is a shortcut
    phi_n = (p - 1) * (q - 1)
    return phi_n

def lcm(a, b):
    """
    Calculate the Least Common Multiple (LCM).

    a: First number.
    b: Second number.

    Returns:
    Least common multiple of a and b.
    """
    return abs(a*b) // bltin_gcd(a, b)

def carmichael_function(p, q):
    """
    Calculate Carmichael's function for the given primes p and q.

    Args:
    p: First prime number.
    q: Second prime number.

    Returns:
    Carmichael's function value for p and q.
    """
    rho_n = lcm((p-1),(q-1))
    return rho_n

def rsa(min, max):
    """
    Implement the RSA key generation based given a range for prime numbers.

    min: Minimum value for prime number generation.
    max: Maximum value for prime number generation.

    Returns:
    Public and private keys.
    """
    # first choose p and q as two prime numbers that are different from each other
    (p,q) = generate_primes(min, max)

    print("generate p and q")

    while p == q:
        q = generate_primes(min, max)
    
    # calculate an n = p * q
    n = p * q
    
    # Eulers totients
    print("totient")
    totient_n = carmichael_function(p, q) #either use gcd or lcm 
    
    # n can be made public, p q and phi stay secret
 
    # pick a public key e such that 2 < e < phi(n) and gcd(e, phi(n) = 1
    print("e")
    e = random.randint(2, totient_n)
    while not coprime2(e, totient_n):
        e = random.randint(2, totient_n)

    # calculate a private key d such that e * d == 1 mod(phi(n)) || e * d mod phi(n) = 1
    print("d")
    d = mod_inverse(e, totient_n)
    
    # public information is e and n 
    # private is d, n, p, and q
    pub = {"e":e, "n":n}
    priv = {"d":d, "n":n, "p": p, "q":q}
    return pub, priv


def encrypt(m, pub):
    """
    Encrypt the message using the public key.

    m: Message to be encrypted.
    pub: Public key (e, n).

    Returns:
    Encrypted message.
    """
    return pow(m, pub["e"], pub["n"])

def decrypt(c, priv):
    """
    Decrypt the message using the private key d.

    c: Encrypted message.
    priv: Private key (d, n, p, q).

    Returns:
    Decrypted message.
    """
    return pow(c,priv["d"], priv["n"] )

def decrypt_CRT(c, priv):  
    """
    Decrypt the message using Chinese Remainder Theorem.
    
    c: Encrypted message.
    priv: Private key (d, n, p, q).

    Returns:
    Decrypted message.
    """
    p = priv["p"]
    q = priv["q"]
    d = priv["d"]
    dq = pow(d, 1, q - 1) 
    dp = pow(d, 1, p - 1) 
    m1 = pow(c, dp, p) 
    m2 = pow(c, dq, q) 
    
    qinv = mod_inverse(q, p) 
    h = (qinv * (m1 - m2)) % p 
    m = m2 + h * q 
    return m 
    
def runthrough(num_times):
    for _ in range(num_times):
        print("generating pub and priv)")
        pub, priv = rsa(2**8, 3**8)
        m = 12345
        print("encrypting")
        c = encrypt(m, pub)
        print("Decrypting")
        m2 = decrypt(c, priv)
        print("DecryptingCRT")
        m3 = decrypt_CRT(c, priv)
        print("Worked?")
        print(m2==m3 and m==m2)
        print("+++++++++++++++++++++++++++++++++++")
# print("generating")
# pub, priv = rsa(2**8, 3**8)
# print(pub, priv)
# m = 13313
# print("encrypt")
# c = encrypt(m, pub)
# print("decrypt")
# m2 = decrypt(c, priv)
# m3 = decrypt_CRT(c, priv)
# print(m2 == m3)
if __name__ == "__main__":
    runthrough(50)