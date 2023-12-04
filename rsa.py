# function to generate random prime integar
import random 
from primePy import primes
from math import gcd as bltin_gcd
from functools import lru_cache

# Memoized using LRU Cache
@lru_cache(maxsize=None)
def generate_prime(min, max):
    available = primes.between(min, max)
    return random.choice(available), random.choice(available)

def coprime2(a, b):
    return bltin_gcd(a, b) == 1

def mod_inverse(e, phi):
    for d in range(3, phi):
        if (d * e) % phi == 1:
            return d
    return ValueError

def euler_totient(p, q):
    #I think that this is a shortcut
    phi_n = (p - 1) * (q - 1)
    return phi_n

def lcm(a, b):
    return abs(a*b) // bltin_gcd(a, b)

def carmichael_function(p, q):
    rho_n = lcm((p-1),(q-1))
    return rho_n

def rsa(min, max):
    #first choose p and q as two prime numbers that are different from each other
	(p,q) = generate_prime(min, max)

	print("generate p and q")

	while p == q:
		q = generate_prime(min, max)
	
	#calculate an n = p * q
	n = p * q
	
	#Eulers totients
	print("totient")
	totient_n = euler_totient(p, q) #either use gcd or lcm 
 
	#n can be made public, p q and phi stay secret
 
	# pick an public key e e such that 2 < e < phi(n) and gcd(e, phi(n) = 1
	print("e")
	e = random.randint(2, totient_n)
	while not coprime2(e, totient_n):
		e = random.randint(2, totient_n)

	# calculate a private key d such that e * d == 1 mod(phi(n)) || e * d mod phi(n) = 1
	print("d")
	d = mod_inverse(e, totient_n)
	
	#public information is e and n 
	#prive is d
	pub = {"e":e, "n":n}
	priv = {"d":d, "n":n}
	return pub, priv

# def encrypt(m, pub):

def encrypt(m, pub):
    return (m ** pub["e"]) % pub["n"]

def decrypt(c, priv):
    return (c ** priv["d"]) % pub["n"]
    
 
print("generating")
pub, priv = rsa(2**8, 3**8)
print(pub, priv)

m = 4
print("encrypt")
c = encrypt(m, pub)
print("decrypt")
m2 = decrypt(c, priv)

print(m == m2)
