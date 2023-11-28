# function to generate random prime integar
import random 
from primePy import primes
from math import gcd as bltin_gcd

def generate_prime(min, max):
    available = primes.between(min, max)
    return random.choice(available)

def coprime2(a, b):
    return bltin_gcd(a, b) == 1

def mod_inverse(e, phi):
    for d in range(3, phi):
        if (d * e) % phi == 1:
            return d
    return ValueError

def rsa(min, max):
    #first choose p and q as two prime numbers that are different from each other
	p = generate_prime(min, max)
	q = generate_prime(min, max)
	while p == q:
		q = generate_prime(min, max)
	
	#calculate an n = p * q
	n = p * q
	
	#Eulers totients
	phi_n = (p - 1) * (q - 1)
 
	#n can be made public, p q and phi stay secret
 
	# pick an public key e e such that 2 < e < phi(n) and gcd(e, phi(n) = 1
	
	e = random.randint(2, phi_n)
	while not coprime2(e, phi_n):
		e = random.randint(2, phi_n)

	# calculate a private key d such that e * d == 1 mod(phi(n)) || e * d mod phi(n) = 1
	d = mod_inverse(e, phi_n)
	
	#public information is e and n 
	#prive is d
	pub = {"e":e, "n":n}
	priv = {"d":d}
	return pub, priv

# def encrypt(m, pub):
    
 
pub, priv = rsa(0, 20)
print(pub, priv)
