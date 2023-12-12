"""
Implementation of RSA attacks (Coppersmith & Weiner)
"""
from rsa import rsa, encrypt, mod_inverse
from sympy import solve, Symbol
from primePy import primes


# Hastad's BroadCast Attack


"""
How Hastad's Attack Works
Basically, we can decipher what M is without needing to know what d is if the following conditions are true

Conditions: 

1. We need to have multiple different ciphertexts (C) generated from the same plaintext (M). Specifically, 
because Hastad's Broadcast works,once the number of ciphertexts > public key, this attack will work work. 

C1 = M^e mod n1
C2 = M^e mod n2
C3 = M^e mod n3


2. These different ciphertexts used multiple different p & q (to generate n1, n2, n3, etc), but the public key (e) is the same
3. The public key is a small value (small public exponent). 


According to CRT, if we calculate n1 * n2 * n3 and divide all of n1, n2, and n3, but this value and subistitute 
"""


def hastad_ciphertexts(message, e):
    """
    Hastad BroadCast Attack ciphertext generators. Will try to implement the Hastad Broadcast 
    Attack given the plaintext & the public key

    message: our plaintext message
    e: our public key

    """

    # generate our public & privates keys, given that public will stay the same for all 3 ciphertexts

    min_range = 2**2
    max_range = 2**8

    #Stores Private Keys
    private_keys= []
    public_keys = []

    for i in range(e):
        pub1, priv1 = rsa(min_range, max_range, e=e)
        inKeys = False


        #If private key is already been generated
        for private in private_keys:
            if priv1["d"] == private["d"]:
                inKeys = True


        while priv1["d"] == ValueError or inKeys:
            inKeys = False
            pub1, priv1 = rsa(min_range, max_range, e=e)

            for private in private_keys:
                if priv1["d"] == private["d"]:
                    inKeys = True

        private_keys.append(priv1)
        public_keys.append(pub1)



    ciphertexts = []
    for key in public_keys:
        ciphertexts.append(encrypt(message, key))

    # Given only ciphertexts, e, and n, we can work back what our original message was
    N=1

    for key in public_keys:
        N = N* key["n"]
    M =0

  



    #CRT

    print("Actual Plaintext:", message)
    for count, key in enumerate(public_keys):

        inversed = mod_inverse(N/key["n"], key["n"]) #50-50 chance of giving us a ValueError because there isn't a 

        print("CipherText", count, ":",  ciphertexts[count], " | Calculating Modular Inverse of N: ", inversed)

        M += ciphertexts[count] * inversed * N/key["n"]


    M = M % N

    m = M**(1.0/e)
    print("Plaintext Approximated from ciphertexts via CRT: ", m)



########################Weiner's Attacks################################################################


def wiener_n(q):
    """Generates p, q, and d where q < p < 2q and d < 1/3(n)^1/4
    
    Args:
        q = some value q that is user inputted. 
        
    Returns:
        two integers, a public and private key that fulfill the Wiener's Attack conditions"""

    #Generating our ranges based on q
    min_range = q
    max_range = 2*q


    pub, priv = rsa(min_range, max_range)
 
    #Find a private key that fulfills initial conditions: 
    while priv["d"] < ((1/3)*(priv["n"])**(1/4)):
        print(priv["d"])
        print((1/3)*(priv["n"])**(1/4))
        pub, priv = rsa(min_range, max_range)

    return pub, priv


def continued_frac(e, N):
    """
    finds continual fractions for e/N and calculates all possible convergents for k/d

    Args:
        e: Public Key
        N = Multiplied value of p * q
    
    Returns:
        A tuple (k, d)
            k is the list of nominators that could potentially be some integer k
            d is the list of corresponding denominators that could potentially be the private key
    """

    #Calculate continued fractions of e/N
    continual_fracs = []
    cf = e // N
    
    r = e % N
    continual_fracs.append(cf)

    while r != 0:
        e, N = N, r
        cf = e // N
        r = e % N

        continual_fracs.append(cf)

    #Verified that this produces the correct value
    #print(continual_fracs)

    #Calculate approximates for k/d
    k = [] # Nominators
    d = [] # Denominators

    for i in range(len(continual_fracs)):
        if i == 0:
            ki = continual_fracs[i]
            di = 1
        elif i == 1:
            ki = continual_fracs[i]*continual_fracs[i-1] + 1
            di = continual_fracs[i]
        else: # i > 1
            ki = continual_fracs[i]*k[i-1] + k[i-2]
            di = continual_fracs[i]*d[i-1] + d[i-2]

        k.append(ki)
        d.append(di)

    return (k, d)



def solve_d(e,n,klist, dlist):
    """
    Finds d from the list of potential d's calculated by convergence. 
    
    1. Use the d value to calculate a phi(n) via 
            phi(n) = ed -1/k
    2. Use phi(n) to calculate a the roots for the solution for  
        x^2 - (n - phi(n)+1)x + n = 0
    3. The roots are p & q, and if they match the chosen n, then we have found the correct private key d
    
    Args:
        e: public key
        n = p * q
        klist: A list of potential integers corresponding to the private keys generated by continual factorization
        dlist: A list of potential private keys generated by continual factorization. 

    Returns:
        A private key
    """

    for key in range(len(klist)):

        #From list of potential private keys, iterate per index
        d = dlist[key]
        k = klist[key]


        if klist[key] != 0:

            #Calculate potential phi_n
            phi_n = (e * d -1)//k


            #Solve quadratic equation to calculate potential p & q
            x = Symbol('x', integer=True)
            roots = solve(x**2 - (n - phi_n + 1)*x + n, x)

            #if p & q exist
            if len(roots) == 2:
                p, q = roots

            

                #if p & q are correct
                if (p * q == n):

                    #Return all data for the private key (d, pq)
                    return (p, q, d)

                
    print("Found nothing")
    return (-1, -1, -1)



def weiner(q):
    """
      Weiner's Theorem (in the context of RSA): Given the public key (e, n), 
    if  q < p < 2q and d < 1/3(n)^1/4 then k/d is amongst the convergences of e/n
    
    Puts everything together for Wiener's Attack
    
    """
    solution = (-1, -1, -1)

    while solution[0] == -1:
        public_key, private_key = wiener_n(q)
        e = public_key["e"]
        n = public_key["n"]
        print(f"Using {q}, generate p: {private_key['p']} public key e:{public_key['e']} and n:{public_key['n']} ")
        k, d = continued_frac(e, n)
        solution = solve_d(e, n, k, d)
    print(solution)
    return solution


if __name__ == "__main__":
    #hastad_ciphertexts(1234, 3)
    #Proof of concept that functions work
    #n = 90581
    #e = 17993
    #k, d = continued_frac(e, n)
    #print(k)
    #[0, 1, 29, 117, 146, 555, 1256, 5579, 17993]
    #print(d)
    #[1, 5, 146, 589, 735, 2794, 6323, 28086, 90581]

    #x = solve_d(e,n, k, d)
    #print (x)
     #(239, 379, 5)
     
    #weiner(6)



